from flask import render_template, Blueprint, flash, request, session, jsonify, make_response
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename
from celery.result import AsyncResult
from converter import save_png_bytes_to_redis
from celeryapp.celery_worker import celery_app
import time
import pprint
from io import BytesIO
from base64 import b64encode

core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def upload_image():

    form = ImageForm()
    if request.method == 'POST' and  form.validate_on_submit():
        if form.submit_send.data:
            img = request.files['image']
            secure_filename(img.filename)
            # save multipart octet to bytes
            img_bytes = BytesIO(img.stream.read())
            task = save_png_bytes_to_redis.delay(img_bytes.getvalue())
            print("TASK ID: ", task.id)
            print("TASK RESULT: ", task.result)

            task_result = save_png_bytes_to_redis.AsyncResult(task.id)
            print("result state: ", task_result.state)
            print("result:", task_result.result)
            img_bytes.close()
            try:
                flash("File uploaded sucessfuly.", category='success')
            except Exception as e:
                flash("Could not upload the file.", category='error')

        return render_template('index.html', form=form)  # redirect(url_for('core.upload_image'))


    if request.method == 'GET':  # testing getting cookies
        try:
            theme = request.cookies.get("theme")
            print(theme)
            session["username"] = "Andrew"
            
        except Exception:
            print("No such cookie.")

    return render_template('index.html', form=form)


@core.route('/info')
def info():
    resp = make_response(render_template('info.html'))
    # resp.set_cookie("theme", "dark")
    # print(session.get("username", None))
    return resp



@core.route('/getresult/<task_id>')
def get_result(task_id):
    task_result = save_png_bytes_to_redis.AsyncResult(task_id)
    print("result state: ", task_result.state)
    print("result:", task_result.result)
    return jsonify({"taskState": task_result.state}), 200


# @core.before_request
# def before_request():
#     try:
#         # connecting to Redis here:
#         g.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=False)  #  TODO: change to 'True' after testing image
#     except redis.exceptions.ConnectionError as err: 
#         print("Connection error occured." , err)


@core.route('/setvar')
def run_task():
    task = save_png_bytes_to_redis.delay("image_data")
    print(task.id)
    insp = celery_app.control.inspect()
    print("TASKS CURRENTLY EXECUTED:")
    pprint.pprint(insp.active())
    print("ACTIVE QUEUES: ")
    pprint.pprint(insp.active_queues())

    return jsonify({"status": "ok", "task_id": task.id})


@core.route("/fetchtest", methods=["GET"])
def fetchtest():
    time.sleep(3)
    return {"some text": "fetch worked!"}

# core.before_request(before_request)