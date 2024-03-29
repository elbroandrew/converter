from flask import Flask
from api.core.views import core
from flask_wtf import CSRFProtect
# from flask_session import Session


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

app.register_blueprint(core)
