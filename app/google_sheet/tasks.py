from config.celery import app

from .task_services import telegram_notification
from .task_services.gsheet_uploader import main


@app.task
def send_message_telegram():
    telegram_notification.send_message()


@app.task
def upload_data_from_gsheet():
    main.upload_gsheet_to_psql()
