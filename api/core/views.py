from flask import render_template, Blueprint, flash, request, session, redirect, url_for, send_file, current_app
from api.core.forms import ImageForm
from werkzeug.utils import secure_filename
from converter import save_png_bytes_to_redis, get_png_image
from io import BytesIO
from pathlib import Path


core = Blueprint('core', __name__)


@core.route('/', methods=['GET', 'POST'])
def upload_image():

    current_app.logger.info("GET REQUEST HIT.")

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
                    current_app.logger.info(f"task: {task}")
                    session["task_id"] = str(task.id)
                    display_download=True
                    file_name = Path(img.filename).stem + ".png"
                    flash("File uploaded sucessfuly.", category='success')
                
            except Exception as e:
                flash("Could not upload the file.", category='error')
                current_app.logger.error(e, f"task status: {task.status}")

            finally:
                img_bytes.close()

    return render_template('index.html', form=form, display_download=display_download, file_name=file_name)



@core.route("/fetchpng", methods=["GET", "POST"])
def fetch_png():
    try:
        if session.get('task_id'):
            task_id = session.get('task_id')
            result_png = get_png_image(task_id)
            session.clear()
            buff = BytesIO(result_png)
            buff.seek(0)
            current_app.logger.info(f"Sent file: status:{task_id.status}, state: {task_id.state}.")
            return send_file(
                buff, 
                mimetype='image/png',
                as_attachment=True,
                download_name="image.png")

        else:
            current_app.logger.error(f"Could not send the file: status:{task_id.status}, state: {task_id.state}.")

    except Exception as e:
        current_app.logger.error(f"Trying fetch png image in 'fetch_png' route", e)
        raise Exception

    return redirect(url_for('core.upload_image'))


@core.route("/info", methods=["GET"])
def info():
    return render_template('info.html')