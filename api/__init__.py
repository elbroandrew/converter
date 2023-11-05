from flask import Flask
from api.core.views import core

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # this limits file size for uploading to 16 MB.

app.register_blueprint(core)