import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError

from . import config


class Extractor:
    """Класс для получение данных из таблицы"""
    CREDENTIALS_JSON = config.CREDENTIALS_JSON
    SCOPES = config.SCOPES
    SAMPLE_SPREADSHEET_ID = config.SAMPLE_SPREADSHEET_ID
    SAMPLE_RANGE_NAME = config.SAMPLE_RANGE_NAME

    def __init__(self):
        self.creds_service = Extractor.__get_service()

    @classmethod
    def __get_service(cls):
        """Подключение к сервису"""
        try:
            creds_service = ServiceAccountCredentials.from_json_keyfile_name(
                cls.CREDENTIALS_JSON, cls.SCOPES).authorize(httplib2.Http())
        except FileNotFoundError:
            print('Файл учетных данных не найден')
        try:
            return creds_service

        except HttpError as err:
            print(err)

    def get_values(self) -> list:
        """Получение данных из таблицы"""
        try:
            sheet = build('sheets', 'v4', http=self.creds_service).spreadsheets()
            result = sheet.values().\
                get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range=self.SAMPLE_RANGE_NAME).execute()

            return result.get('values', [])

        except HttpError as err:
            print(err)

    def get_file_changes(self) -> str:
        """Получение даты последней модификации файла"""
        service = build('drive', 'v2', http=self.creds_service)
        return service.files().get(fileId=self.SAMPLE_SPREADSHEET_ID).execute().get('modifiedDate')
