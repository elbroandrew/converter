# Login Form in the Auth Service
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators



class LoginForm(FlaskForm):

    name = StringField('Name', validators=[validators.InputRequired()]) 
    password = PasswordField('Password', validators=[validators.InputRequired()]) 
