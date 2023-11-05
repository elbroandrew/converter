import pathlib
from flask import render_template, Blueprint, redirect, url_for, flash, request
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def upload_image():
    '''
    This is the home page view.
    '''
    btn=False
    form = ImageForm()
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
            
        if form.download.data:
            print("DOWNLOADING IMAGE.")
        print(btn)
        return render_template('index.html', form=form, btn=btn)  # redirect(url_for('core.upload_image'))
    print("btn :%s" % btn)            

    return render_template('index.html', form=form, btn=btn)


@core.route('/info')
def info():
    '''
    Example view of any other "core" page.
    '''
    return render_template('info.html')

