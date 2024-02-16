from celery import Celery, Task


celery_app = Celery(__name__)
celery_app.conf.broker_url = "redis://0.0.0.0:6379/0"
celery_app.conf.result_backend = 'redis://localhost:6379/0'
