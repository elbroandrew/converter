import os
from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, current_user
from models.users import User


auth = Flask(__name__)
auth.config['SECRET_KEY'] = 'secretkey'  # put it in env file, must be the same as for 'api' service
dbasedir = os.path.abspath(os.path.dirname(__file__))
auth.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(dbasedir, "data.sqlite")
auth.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
auth.config["JWT_SECRET_KEY"] = "jwtsecretkey"  # put it in env file, must be the same as for 'api' service


db = SQLAlchemy(auth)
jwt = JWTManager(auth)
Migrate(auth, db)  


@auth.route("/", methods=["GET"])
def index():
    return render_template("home.html")


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id



@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


@auth.route("/whoami", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        username=current_user.username,
        is_admin=current_user.is_admin
    )




if __name__ == '__main__':

    auth.run(host="127.0.0.1", debug=False, port=5006)   #  make  0.0.0.0