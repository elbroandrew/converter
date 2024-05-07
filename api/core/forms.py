from flask_wtf import FlaskForm
from wtforms import SubmitField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ImageForm(FlaskForm):
    image = FileField('image', validators=[
        FileRequired(),
        validators.InputRequired(),
        FileAllowed(['blp'], ".BLP files only required!")
    ])
    submit_send = SubmitField(label="convert image")
