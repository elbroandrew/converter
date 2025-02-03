from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for, flash, make_response
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                jwt_required, set_access_cookies, set_refresh_cookies
                                )
from flask_jwt_extended import get_jwt
from models.users import User
from forms import LoginForm, RegistrationForm
from initialize import jwt, db, app

auth_api = Blueprint("auth_api", __name__)


@auth_api.route("/", methods=["GET"])
def index():
    return render_template("home.html")

@auth_api.route("/welcome", methods=["GET"])  #TODO: REMOVE WELCOME PAGE & REDIRECT TO API HOME PAGE
@jwt_required(optional=True)
def welcome():
    claims = get_jwt()
    username = claims.get("username", None)
    if not username:
        return abort(401)

    return render_template("welcome.html", username=username)

@app.errorhandler(404)   # TODO: check 404 page with blueprint
def pageNotFound(error):
    return render_template("page404.html", data="Page Not Found."), 404

@auth_api.errorhandler(409)
def conflictPage(error):
    return render_template("page409.html"), 409

@auth_api.errorhandler(401)
def pageError401(error):
    return render_template("page401.html"), 401

@jwt.unauthorized_loader
def unauthorized_handler(f):
    return make_response(render_template("page401.html"), 401)


@auth_api.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    if request.method == "POST" and form.validate_on_submit():
        user: User = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            user = User(email=form.email.data, username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Thanks for registration!")
            
            access_token = create_access_token(identity=user.id, additional_claims={"username":user.username, 
                                                                                "email":user.email,
                                                                                "password_hash": user.password_hash})
            refresh_token = create_refresh_token(identity=user.id, additional_claims={"username":user.username, 
                                                                                "email":user.email,
                                                                                "password_hash": user.password_hash})
            resp = make_response(redirect(url_for("auth_api.welcome", username=user.username)))
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp, 301
        else:
            abort(409)
        
    return render_template("register.html", form=form)


@jwt.user_identity_loader
def user_identity_lookup(id):
    return id



@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@auth_api.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user: User = User.query.filter_by(email=form.email.data).one_or_none()

        if not user or not user.check_password(form.password.data):
            return abort(401)

        access_token = create_access_token(identity=user.id, additional_claims={"username":user.username, 
                                                                                "email":user.email,
                                                                                "password_hash": user.password_hash})
        refresh_token = create_refresh_token(identity=user.id, additional_claims={"username":user.username, 
                                                                                "email":user.email,
                                                                                "password_hash": user.password_hash})
        resp = make_response(redirect(url_for("auth_api.welcome", username=user.username)))  # redirect to API home page ?
        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)
        return resp, 301

    return render_template("login.html", form=form)


@auth_api.route("/who", methods=["GET", "POST"])
@jwt_required()
def protected():

    claims = get_jwt()
    user_id = claims["sub"]
    username = claims.get("username", None)
    if not username:
        return abort(401)
    
    return jsonify(logged_in_as=username, id=user_id), 200

