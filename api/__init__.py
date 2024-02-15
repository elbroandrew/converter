from flask import Flask
# from flask import g
from api.core.views import core
from flask_wtf import CSRFProtect
# from flask_session import Session
# import redis
from celery import Celery


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  # it is for client session cookie; if I use Flask-Session I don't need the 'secret' key. Cannot be deleted. 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # this limits file size for uploading to 16 MB.
# setup session for redis
# app.config['SESSION_TYPE'] = 'redis'
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_USE_SIGNER"] = True
# app.config["SESSION_REDIS"] = redis.from_url("redis://127.0.0.1:6379")

csrf = CSRFProtect(app)

# server_session = Session(app)

app.config["CELERY_BROKER_URL"] = "redis://127.0.0.1:6379/"
app.config["CELERY_RESULT_BACKEND"] = 'redis://localhost:6379/'

celery_app = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery_app.conf.update(app.config)

app.register_blueprint(core)
