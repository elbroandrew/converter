from flask import render_template, Blueprint, flash, request, session, jsonify, redirect, url_for, send_file
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename
from converter import save_png_bytes_to_redis, get_png_image
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
                print(task)              
                if task.get():
                    print("task get")
                    session["task_id"] = str(task.id)
                    display_download=True
                    file_name = Path(img.filename).stem + ".png"
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
    task = current_app.AsyncResult(task_id)
    return jsonify({
        "uuid": session["user_uuid"],
        "task_id": task_id,
        "task_result": str(task.result)
        }), 200




@core.route("/fetchpng", methods=["GET", "POST"])
def fetch_png():
    try:
        if session.get('task_id'):
            print("GETTING PNG IMAGE....")
            task_id = session.get('task_id')
            result_png = get_png_image(task_id)
            session.clear()
            buff = BytesIO(result_png)
            buff.seek(0)
            return send_file(
                buff, 
                mimetype='image/png',
                as_attachment=True,
                download_name="image.png")

        else:
            print("ERROR: cannot fetch png.")
    except Exception as e:
        print("ERROR OCCURED: ")
        print(e)


    return redirect(url_for('core.upload_image'))