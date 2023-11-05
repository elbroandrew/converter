import pathlib
from flask import render_template, Blueprint, redirect, url_for, flash
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename

core = Blueprint('core', __name__)

@core.route('/', methods=[ 'POST'])
def upload_image():
    '''
    This is the home page view.
    '''
    form = ImageForm()
    if form.validate_on_submit():
        img = form.image.data
        filename = secure_filename(img.filename)
        project_dir = pathlib.Path(__file__).resolve()
        save_path = project_dir.parent.parent/"assets"/filename
        try:
            img.save(save_path)
        
        flash("File uploaded sucessfuly.")
        return redirect(url_for('core.index'))

    return render_template('index.html', form=form)

@core.route('/', methods=['GET'])
def index():
    form = ImageForm()
    return render_template('index.html', form=form)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page.
    '''
    return render_template('info.html')

