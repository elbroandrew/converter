from flask import Flask
from api.core.views import core
from flask_wtf import CSRFProtect
from datetime import timedelta
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "file": {
                "class": "logging.FileHandler",
                "filename": "flask.log",
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["file"]},
    }
)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  # it is for client session cookie; if I use Flask-Session I don't need the 'secret' key. Cannot be deleted. 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # this limits file size for uploading to 16 MB.
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=3)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = True


csrf = CSRFProtect(app)


app.register_blueprint(core)
