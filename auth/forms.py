# Login Form in the Auth Service
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField, validators



class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[validators.InputRequired()])
    email = EmailField()
    password = PasswordField('Password', validators=[validators.InputRequired()]) 




class LoginForm(FlaskForm):

    name = StringField('Name', validators=[validators.InputRequired()]) 
    password = PasswordField('Password', validators=[validators.InputRequired()]) 
