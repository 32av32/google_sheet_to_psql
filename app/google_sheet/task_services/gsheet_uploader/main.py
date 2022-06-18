from os import environ

import psycopg2
from dotenv import load_dotenv

from .google_sheet_extracter import google_sheet_extracter
from .postgres_loader import transformer, loader
from .utils import state

PATH_STATE_FILE_STORAGE = 'state.json'
# Позиция в таблице для значения "Стоимость"
CURRENCY_POSITION = 2
# Позиция в таблице столбца с уникальными значенями
UNIQUE_COLUMN_POS = 1

load_dotenv()
dsn = {
    'dbname': environ.get('DB_NAME'),
    'user': environ.get('DB_USER'),
    'password': environ.get('DB_PASSWORD'),
    'host': environ.get('DB_HOST', 'localhost'),
    'port': environ.get('DB_PORT', 5432),
}

file_storage = state.JsonFileStorage(PATH_STATE_FILE_STORAGE)
state_control = state.State(file_storage)

extractor = google_sheet_extracter.Extractor()


def upload_gsheet_to_psql():
    # Получение даты модификации последнего загруженного файла
    file_date_modified = state_control.get_state('file_date_modified')
    # Получение даты последней модификации файла
    date_changes = extractor.get_file_changes()
    if file_date_modified != date_changes:
        # Получение значений из таблицы
        data = extractor.get_values()
        # Трансформация данных для загрузки в БД
        data_transformer = transformer.Transformer(data=data, currency_position=CURRENCY_POSITION)
        data_transformer.transform_data()
        # Загрузка данных в БД
        try:
            with psycopg2.connect(**dsn) as conn:
                data_loader = loader.PostgresLoader(conn, data)
                data_loader.upload_data(unique_column_pos=UNIQUE_COLUMN_POS)
                # Сохранение состояния даты модификации
                state_control.set_state('file_date_modified', date_changes)
        except psycopg2.OperationalError as err:
            print(err)


if __name__ == '__main__':
    upload_gsheet_to_psql()
