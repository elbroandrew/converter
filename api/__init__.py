from flask import Flask
from api.core.views import core

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

app.register_blueprint(core)