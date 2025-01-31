from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, validators


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[validators.InputRequired(), validators.DataRequired()])
    email = EmailField("Email", validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.InputRequired(), validators.DataRequired(), validators.EqualTo("pass_confirm")])
    pass_confirm = PasswordField("Confirm Password", validators=[validators.DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.InputRequired()])
    submit = SubmitField('Log in')
    