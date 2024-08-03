import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam': {
        'task' : 'general.tasks.send_mail',
        'schedule': crontab(minute=0, hour=21),
    },
    'send-spam1': {
        'task' : 'general.tasks.send_mail',
        'schedule': crontab(minute=0, hour=8),
    },
}