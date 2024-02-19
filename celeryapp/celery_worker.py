from celery import Celery, Task


celery_app = Celery(__name__, backend="redis://0.0.0.0:6379/0", broker="redis://0.0.0.0:6379/0", include=['converter.converter'])
celery_app.set_default()
celery_app.conf.task_track_started = True
celery_app.conf.ignore_result = False
# celery_app.conf.broker_url = "redis://0.0.0.0:6379/0"
# celery_app.conf.result_backend = 'redis://0.0.0.0:6379/0'
