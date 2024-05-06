from flask import render_template, Blueprint, flash, request, session, jsonify, make_response, app
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename
from celery.result import AsyncResult
from converter import save_png_bytes_to_redis
from celeryapp.celery_worker import celery_app
import time
from uuid import uuid4
import pprint
from io import BytesIO
from celery import current_app


core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def upload_image():

    form = ImageForm()
    if request.method == 'POST' and  form.validate_on_submit():

        session.permanent = True

        if form.submit_send.data:

            user_uuid = str(uuid4())
            session["user_uuid"] = user_uuid

            img = request.files['image']
            secure_filename(img.filename)
            # save multipart octet to bytes
            img_bytes = BytesIO(img.stream.read())
            task = save_png_bytes_to_redis.delay(img_bytes.getvalue())
            session["task_id"] = str(task.id)
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


    # if request.method == 'GET':  # testing getting cookies
    #     try:
    #         theme = request.cookies.get("theme")
    #         print(theme)
    #         session["username"] = "Andrew"
            
    #     except Exception:
    #         print("No such cookie.")

    return render_template('index.html', form=form)


@core.route('/info')
def info():
    # resp.set_cookie("theme", "dark")
    # print(session.get("username", None))
    _task_id_ = session['task_id']
    task = current_app.AsyncResult(_task_id_)
    print(current_app.AsyncResult(_task_id_))
    print(task.get())
    return render_template('info.html', taskId=_task_id_)



@core.route('/getresult/<task_id>')
def get_result(task_id):
    # task_result = save_png_bytes_to_redis.AsyncResult(task_id)
    task = current_app.AsyncResult(task_id)
    print(task.get())
    print("user_uuid: ", session["user_uuid"])
    return jsonify({
        "uuid": session["user_uuid"],
        "task_id": task_id,
        "task_result": str(task.result)
        }), 200




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
