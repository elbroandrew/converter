import pathlib
from flask import render_template, Blueprint, redirect, url_for, flash, request
from api.core.forms import ImageForm, DownloadForm
from werkzeug.utils import secure_filename

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def upload_image():
    '''
    This is the home page view.
    '''
    filename=None
    btn=False
    form = ImageForm()
    form_download = DownloadForm()
    if request.method == 'POST' and  form.validate_on_submit():
        if form.send.data:
            img = form.image.data
            filename = secure_filename(img.filename)
            project_dir = pathlib.Path(__file__).resolve()
            save_path = project_dir.parent.parent/"assets"/filename
            try:
                img.save(save_path)
                flash("File uploaded sucessfuly.")
                btn=True
            except Exception:
                flash("Could not upload the file.")
            
        print(btn)
        print(filename)
        return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=filename)  # redirect(url_for('core.upload_image'))
    print("btn :%s" % btn)

    if request.method == 'POST' and  form_download.validate_on_submit():
            print("DOWNLOADING IMAGE.")    

    return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=filename)


@core.route('/info')
def info():
    '''
    Example view of any other "core" page.
    '''
    return render_template('info.html')

