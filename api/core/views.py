from flask import render_template, Blueprint, flash, request, session, jsonify, redirect, url_for
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename
from converter import save_png_bytes_to_redis
from celeryapp.celery_worker import celery_app
import time
import pprint
from io import BytesIO
from celery import current_app
from pathlib import Path


core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def upload_image():

    form = ImageForm()
    display_download = False
    file_name = ""
    if request.method == 'POST' and  form.validate_on_submit():

        session.permanent = True

        if form.submit_send.data:

            try:
                img = request.files['image']
                secure_filename(img.filename)
                # save multipart octet to bytes
                img_bytes = BytesIO(img.stream.read())
                task = save_png_bytes_to_redis.delay(img_bytes.getvalue())                
                if task.get():
                    session["task_id"] = str(task.id)
                    display_download=True
                    file_name = Path(img.filename).stem + ".png"
                print("STATUS======>",task.status)
                print("TASK ID: ", task.id)
                flash("File uploaded sucessfuly.", category='success')
                
            except Exception as e:
                flash("Could not upload the file.", category='error')
                print(e)
                print(task.status, task.state)

            finally:
                img_bytes.close()

    return render_template('index.html', form=form, display_download=display_download, file_name=file_name)


@core.route('/info')
def info():
    if session.get('task_id'):
        _task_id_ = session['task_id']
        task = current_app.AsyncResult(_task_id_)
        print(current_app.AsyncResult(_task_id_))
        print(task.get())
        return render_template('info.html', taskId=_task_id_)
    
    return render_template('info.html', taskId="PNG IMAGE IS NOT READY YET.")



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

@core.route("/fetchpng", methods=["GET"])
def fetch_png():
    
    return redirect(url_for('core.upload_image'))