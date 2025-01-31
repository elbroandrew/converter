from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = EmailField("Email", validators=[Email(), 
                                            DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired(),                                                                  
                                                    EqualTo("password", message="Passwords must match.")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
    