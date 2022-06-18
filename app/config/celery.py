from os import environ
from celery import Celery
from celery.schedules import crontab

environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'google_sheet-every-1-hour': {
        'task': 'google_sheet.tasks.upload_data_from_gsheet',
        'schedule': crontab(minute='*/1'),
    },
    'google_sheet-every-24-hour': {
        'task': 'google_sheet.tasks.send_message_telegram',
        'schedule': crontab(minute='*/1'),
    },
}
