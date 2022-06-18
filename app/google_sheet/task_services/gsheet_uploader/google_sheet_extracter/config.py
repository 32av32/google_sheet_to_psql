import os


# Список прав.
SCOPES = ('https://www.googleapis.com/auth/spreadsheets.readonly',
          'https://www.googleapis.com/auth/drive.metadata.readonly',)
# ID и диапазон таблицы.
SAMPLE_SPREADSHEET_ID = '1ZfyePpM3GgpYrswZMNzEQN9RjxCYfAHUrbSxs8MKn08'
SAMPLE_RANGE_NAME = 'Лист1!A2:D'
# Файл сервис аккаунта
CREDENTIALS_JSON = os.path.dirname(__file__) + '.json'
