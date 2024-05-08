from PIL import Image
from io import BytesIO
from celeryapp.celery_worker import celery_app


@celery_app.task(name="CONVERT BLP IMAGE INTO PNG")
def save_png_bytes_to_redis(img_bytes):
    
    im = Image.open(BytesIO(img_bytes))
    png_bytes = convert_blp_to_png_bytes(im)
    return png_bytes


def convert_blp_to_png_bytes(img) -> BytesIO:
    """
    img is BLP image
    """
    buff = BytesIO()
    img.save(buff, format='png')  # save to buffer, not to disk
    png_bytes: bytes = buff.getvalue()
    buff.close()
    return png_bytes

@celery_app.task(name="DOWNLOAD PNG IMAGE FROM REDIS INSTANCE")
def get_png_image(task_id):
    task = celery_app.AsyncResult(task_id)
    png_bytes = task.result
    buff = BytesIO()
    new_image = Image.open(BytesIO(png_bytes))
    new_image.save(buff, format='png')
    PNG = buff.getvalue()
    return png_bytes

