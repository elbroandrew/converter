from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ImageForm(FlaskForm):
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['blp'], ".BLP files only required!")
    ])
    send = SubmitField(label="convert image")
    # download = SubmitField(label='download')


class DownloadForm(FlaskForm):
    download = SubmitField(label='download')