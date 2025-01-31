import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secretkey'  # put it in env file, must be the same as for 'api' service
dbasedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(dbasedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "jwtsecretkey"  # put it in env file, must be the same as for 'api' service

#TODO: init DB first
db = SQLAlchemy(app)
jwt = JWTManager(app)
Migrate(app, db)
