Задача выплонена в виде Django проекта. В приложении google_sheet добавлены задачи Celery для загрузки данных (upload_data_from_gsheet) и отправки сообщений (send_message_telegram). Периодичность задач поставлен на 1 минуту (для теста). Реализации функций находятся в приложении google_sheet в виде модуля task_services. Для работы сервиса необходимы виртуальные переменные:

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_ENGINE=

TELEGRAMBOT_TOKEN=
TELEGRAM_CHAT_ID=

SECRET_KEY=
ALLOWED_HOSTS=

Для сервиса загрузки файлов по адресу app/google_sheet/task_services/gsheet_uploader/google_sheet_extracter находится файл конфигурации config. В данную директорую необходимо загрузить файл api_key сервисного аккаунта google и прописать имя файла в конфигурации.



P.S.
Так как не нашел api для отслеживания изменений в строках и так как в таблице отсутствовали записи о дате модификации строки, при изменении файла, таблица загружается в БД полностью со всеми изменениями. 

