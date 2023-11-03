from flask import Flask
from converter.core.views import core

app = Flask(__name__)

app.register_blueprint(core)