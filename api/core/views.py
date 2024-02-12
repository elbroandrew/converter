import redis
from flask import render_template, Blueprint, flash, request, session, send_file
from api.core.forms import ImageForm, DownloadForm
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO
from converter import *
from flask import make_response

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
            secure_filename(img.filename)
            # save multipart octet to bytes
            image_bytes = BytesIO(img.stream.read())
            save_img_bytes_to_redis(image_bytes)  # test, set var
            # image = Image.open(image_bytes)
            try:
                # image.save("converter/output.png")
                #return send_file(image, download_name="output.png",  as_attachment=True)
                image_bytes.close()
                flash("File uploaded sucessfuly.", category='success')
                btn=True
            except Exception as e:
                flash("Could not upload the file.", category='error')
                # print(e)
            
        # print(btn)
        # print(image)
        return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=f"{filename}.png")  # redirect(url_for('core.upload_image'))
    # print("btn :%s" % btn)

    if request.method == 'POST' and  form_download.submit.data:
        print("download form is submitted: %s" % form_download.is_submitted())
        print(f"download form validate: {form_download.validate()}")
        print(f"download form data: {form_download.submit.data}")
        if image:
            print(f"DOWNLOADING IMAGE: {image}")
        else:
            print("NOTHING TO DOWNLOAD.")

    if request.method == 'GET':  # testing getting cookies
        try:
            theme = request.cookies.get("theme")
            print(theme)
            session["username"] = "Andrew"
            
        except Exception:
            print("No such cookie.")

    return render_template('index.html', form=form, form_download=form_download, btn=btn, filename=filename)
# session:"eyJjc3JmX3Rva2VuIjoiZmJkNzc5MDk0Y2U2MjkyMDM3YzcyZGI5MzYwZjViOGUzNjMwNzQzNiJ9.ZcXkVA.l-zmbCORV28n_GcJwpbxyzw3nQs"
# session:"eyJjc3JmX3Rva2VuIjoiZmJkNzc5MDk0Y2U2MjkyMDM3YzcyZGI5MzYwZjViOGUzNjMwNzQzNiIsInVzZXJuYW1lIjoiQW5kcmV3In0.ZcXmiA.qEQ3yQukWyJETCcj4xiOcU_4TP8"

@core.route('/info')
def info():
    resp = make_response(render_template('info.html'))
    # resp.set_cookie("theme", "dark")
    print(session.get("username", None))
    return resp



@core.route('/getvar')
def getvar():
    return g.redis_client.get('foo')


@core.before_request
def before_request():
    try:
        # connecting to Redis here:
        g.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=False)  #  TODO: change to 'True' after testing image
    except redis.exceptions.ConnectionError as err: 
        print("Connection error occured." , err)
        


# register a 'before request handler' & 'teardown request'
core.before_request(before_request)