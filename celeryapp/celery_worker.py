from celery import Celery


celery_app = Celery(__name__, backend="redis://0.0.0.0:6379/0", broker="redis://0.0.0.0:6379/0")
celery_app.set_default()
celery_app.conf.task_track_started = True
celery_app.conf.ignore_result = False
