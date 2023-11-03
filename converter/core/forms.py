from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ImageForm(FlaskForm):
    image = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['blp'], ".BLP files only required!")
    ])

 