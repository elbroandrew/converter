from celery import Celery, Task
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config["CELERY_BROKER_URL"] = "redis://127.0.0.1:6379/"
    app.config["CELERY_RESULT_BACKEND"] = 'redis://localhost:6379/'

    celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
    celery.conf.update(app.config)

    return celery