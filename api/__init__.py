from flask import Flask
# from flask import g
from api.core.views import core
from flask_wtf import CSRFProtect
from celery import Celery
# from flask_session import Session
# import redis


def celery_config():
    app = Flask(__name__)
    app.config["CELERY_BROKER_URL"] = "redis://127.0.0.1:6379/0"
    app.config["CELERY_RESULT_BACKEND"] = 'redis://localhost:6379/'

    return app.config

def create_app():
    """Create a Flask application + celery
    """


    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'  # it is for client session cookie; if I use Flask-Session I don't need the 'secret' key. Cannot be deleted. 
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # this limits file size for uploading to 16 MB.
    # setup session for redis
    # app.config['SESSION_TYPE'] = 'redis'
    # app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_USE_SIGNER"] = True
    # app.config["SESSION_REDIS"] = redis.from_url("redis://127.0.0.1:6379")
 ##   app.config["CELERY_BROKER_URL"] = "redis://127.0.0.1:6379/0"
 ##   app.config["CELERY_RESULT_BACKEND"] = 'redis://localhost:6379/'
    csrf = CSRFProtect(app)

    # server_session = Session(app)

    ##celery_app = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
    ##celery_app.conf.update(app.config)

    # app.config.from_mapping(
    #     CELERY=dict(
    #         broker_url="redis://localhost:6379",
    #         result_backend="redis://localhost:6379",
    #     ),
    # )

    # celery_app = Celery(app.name)
    # celery_app.config_from_object(app.config["CELERY"])
    # celery_app.set_default()
    # app.extensions["celery"] = celery_app

    app.register_blueprint(core)

base_config = celery_config()

celery = Celery(__name__, broker=base_config["CELERY_BROKER_URL"])