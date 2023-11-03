import pathlib
from flask import render_template, request, Blueprint, redirect, url_for
from converter.core.forms import ImageForm
from werkzeug.utils import secure_filename

core = Blueprint('core', __name__)

@core.route('/index', methods=['GET', 'POST'])
def upload_image():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    form = ImageForm()
    if form.validate_on_submit():
        img = form.image.data
        filename = secure_filename(img.filename)
        project_dir = pathlib.Path(__file__).resolve()
        save_dir = file_path.parent.parent/"assets"/filename
        img.save(save_dir)
        return redirect(url_for('core.index'))

    return render_template('index.html', form=form)

@core.route('/info')
def info():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    return render_template('info.html')

