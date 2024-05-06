from flask import Flask
from api.core.views import core
from flask_wtf import CSRFProtect
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  # it is for client session cookie; if I use Flask-Session I don't need the 'secret' key. Cannot be deleted. 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # this limits file size for uploading to 16 MB.
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=3)

csrf = CSRFProtect(app)


app.register_blueprint(core)
