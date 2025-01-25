import os
from celery import Celery
from celery.schedules import crontab
# from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'config.settings')

app = Celery('config')
# app = Celery('config', broker=settings.CELERY_BROKER_URL)


app.config_from_object(f'django.conf:settings', namespace='CELERY')
# app.conf.broker_url = 'redis://redis:6379/0'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam': {
        'task' : 'general.tasks.send_mail',
        'schedule': crontab(minute=0, hour=21),
    },
    'send-spam1': {
        'task' : 'general.tasks.send_mail',
        'schedule': crontab(minute=0, hour=9),
    },
    'send-spam3': {
        'task' : 'general.tasks.send_graf',
        'schedule': crontab(day_of_week='sun')
    },
}
#day_of_week='sun'