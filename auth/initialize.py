import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_cors import CORS
from datetime import timedelta


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secretkey'  # put it in env file, must be the same as for 'api' service
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+mysqlconnector://username:passwd@mysql:3306/auth_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "jwtsecretkey"  # put it in env file, must be the same as for 'api' service
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=30)


db = SQLAlchemy(app)
jwt = JWTManager(app)
Migrate(app, db)
