import pathlib
from flask import render_template, Blueprint, flash, request
from api.core.forms import ImageForm, DownloadForm
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO
import numpy as np


core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def upload_image():
    '''
    This is the home page view.
    '''
    image = None
    filename=None
    btn=False
    form = ImageForm()
    form_download = DownloadForm()
    if request.method == 'POST' and  form.validate_on_submit():
        if form.send.data:
            img = request.files['image']
            filename = secure_filename(img.filename)
            project_dir = pathlib.Path(__file__).resolve()
            save_path = project_dir.parent.parent/"assets"/filename
            # save multipart octet to bytes
            image_bytes = BytesIO(img.stream.read())
            image = Image.open(image_bytes)

            try:
                image.save("converter/output.png")
                flash("File uploaded sucessfuly.")
                btn=True
            except Exception as e:
                flash("Could not upload the file.")
                print(e)
            
        print(btn)
        print(image)
        return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=filename)  # redirect(url_for('core.upload_image'))
    print("btn :%s" % btn)

    if request.method == 'POST' and  form_download.validate_on_submit():
            if image:
                print(f"DOWNLOADING IMAGE: {image}")
            else:
                 print("NOTHING TO DOWNLOAD.")


    return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=filename)


@core.route('/info')
def info():
    '''
    Example view of any other "core" page.
    '''
    return render_template('info.html')

