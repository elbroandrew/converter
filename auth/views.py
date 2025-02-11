from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for, flash, make_response
from flask_jwt_extended import (create_access_token, create_refresh_token, 
                                jwt_required, set_access_cookies, set_refresh_cookies
                                )
from flask_jwt_extended import get_jwt, unset_jwt_cookies
from models.users import User
from forms import LoginForm, RegistrationForm
from initialize import jwt, db, app
from datetime import datetime
from datetime import timedelta
from datetime import timezone


auth_api = Blueprint("auth_api", __name__)


@auth_api.route("/", methods=["GET"])
@jwt_required(optional=True)
def index():
    claims = get_jwt()
    if claims:
        username = claims.get("username", None)
        return render_template("welcome.html", username=username)
    return render_template("home.html")

@auth_api.route("/welcome", methods=["GET"])  #TODO: REMOVE WELCOME PAGE & REDIRECT TO API HOME PAGE
@jwt_required(optional=True)
def welcome():
    claims = get_jwt()
    username = claims.get("username", None)
    if not username:
        return abort(401)

    return render_template("welcome.html", username=username)

@app.errorhandler(404)   #errorhandler for 404 page to work with blueprint
def pageNotFound(error):
    return render_template("page404.html", data="Page Not Found."), 404

@auth_api.errorhandler(409)
def conflictPage(error):
    return render_template("page409.html"), 409

@auth_api.errorhandler(401)
def pageError401(error):
    print("ERROR::401")
    return render_template("page401.html"), 401

@jwt.unauthorized_loader   # error page when JWT is valid, but the user is not authorized to get the resource
def unauthorized_handler(f):
    print("ERROR::401::UNAUHTORIZED")
    return make_response(render_template("page401.html"), 401)

@jwt.expired_token_loader
def expired_token_handler(jwt_header, jwt_data):
    print("TOKEN EXPIRED, REDIRECT TO '/refresh'", flush=True)
    return redirect(url_for("auth_api.refresh")), 301
    
@auth_api.route("/refresh", methods=["POST", "GET"])
@jwt_required(refresh=True)
def refresh():
    claims = get_jwt()
    print("REFRESH CLAIMS:: ",claims, flush=True)
    username = claims.get("username")
    user_id = claims.get("sub")
    email = claims.get("email")
    password_hash=claims.get("password_hash")
    access_token = create_access_token(identity=user_id, additional_claims={"username":username, 
                                                                                "email":email,
                                                                                "password_hash": password_hash})
    resp = make_response(redirect(url_for("auth_api.index", username=username)))
    set_access_cookies(resp, access_token)
    return resp, 301


@auth_api.route("/register", methods=["GET", "POST"])
@jwt_required(optional=True)
def register():
    form = RegistrationForm()
    claims = get_jwt()
    if claims:
        flash("You are currently logged in.")
        return render_template("welcome.html", username=claims.get("username"))
    if request.method == "POST" and form.validate_on_submit():
        user: User = db.session.query(User).filter((User.username==form.username.data) | (User.email==form.email.data)).one_or_none()
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


@auth_api.route("/login", methods=["GET", "POST"])
@jwt_required(optional=True)
def login():
    claims = get_jwt()
    if claims:
        flash("You are currently logged in.")
        return render_template("welcome.html", username=claims.get("username"))
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user: User = User.query.filter_by(email=form.email.data).one_or_none()

        if not user or not user.check_password(form.password.data):
            return abort(401)

        access_token = create_access_token(identity=user.id, additional_claims={"username":user.username, 
                                                                                "email":user.email,
                                                                                "password_hash": user.password_hash}, 
                                                                                )
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
    print("ACCESS TOKEN:: ",claims, flush=True )
    user_id = claims["sub"]
    username = claims.get("username", None)
    exp_time = claims.get("exp")
    print("EXP TIME:: ", exp_time, flush=True)
    if not username:
        return abort(401)
    
    return jsonify(logged_in_as=username, id=user_id), 200


@auth_api.route("/logout", methods=["POST", 'GET'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]




