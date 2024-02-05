import pathlib
import redis
from flask import render_template, Blueprint, flash, request, send_file,  stream_with_context, Response
from flask import g
from api.core.forms import ImageForm, DownloadForm
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO


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
        if form.submit_send.data:
            img = request.files['image']
            filename = secure_filename(img.filename)
            #project_dir = pathlib.Path(__file__).resolve()
            #save_path = project_dir.parent.parent/"images"/filename
            # save multipart octet to bytes
            image_bytes = BytesIO(img.stream.read())
            image = Image.open(image_bytes)
            # filename = filename.split('.')[0]
            try:
                #image.save("converter/output.png")
                return send_file(image, download_name="output.png",  as_attachment=True)
                image_bytes.close()
                flash("File uploaded sucessfuly.", category='success')
                btn=True
            except Exception as e:
                flash("Could not upload the file.", category='error')
                print(e)
            
        print(btn)
        print(image)
        return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=f"{filename}.png")  # redirect(url_for('core.upload_image'))
    print("btn :%s" % btn)

    if request.method == 'POST' and  form_download.submit.data:
        print("download form is submitted: %s" % form_download.is_submitted())
        print(f"download form validate: {form_download.validate()}")
        print(f"download form data: {form_download.submit.data}")
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

@core.route('/setvar')
def setvar():
    g.redis_client.set('foo', 'bar')
    return "set foo"


@core.route('/getvar')
def getvar():
    return g.redis_client.get('foo')


@core.before_request
def before_request():
    try:
        g.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
    except redis.exceptions.ConnectionError as err: 
        print("Connection error occured." , err)
        


# register a 'before request handler' & 'teardown request'
core.before_request(before_request)