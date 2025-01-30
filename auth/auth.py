import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy



auth = Flask(__name__)
auth.config['SECRET_KEY'] = 'secretkey'  # put it in env file, must be the same as for 'api' service
dbasedir = os.path.abspath(os.path.dirname(__file__))
auth.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(dbasedir, "data.sqlite")
auth.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
auth.config["JWT_SECRET_KEY"] = "jwtsecretkey"


db = SQLAlchemy(auth)
Migrate(auth, db)





if __name__ == '__main__':

    auth.run(host="127.0.0.1", debug=False, port=5006)   #  make  0.0.0.0