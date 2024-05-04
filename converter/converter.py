from PIL import Image
from io import BytesIO
from celeryapp.celery_worker import celery_app
import time


@celery_app.task(name="CONVERT BLP IMAGE INTO PNG")
def save_png_bytes_to_redis(img):

    # save multipart octet to bytes
    img_bytes = BytesIO(img.stream.read())
    im = Image.open(img_bytes)
    png_bytes = convert_blp_to_png_bytes(im)
    img_bytes.close()
    print("CONVERTING IMAGE BLP TO BYTES_IO")
    time.sleep(4)
    return png_bytes


def convert_blp_to_png_bytes(img) -> BytesIO:
    """
    img is BLP image
    """
    # im = Image.open(img_bytes)
    buff = BytesIO()
    img.save(buff, format='png')  # save to buffer, not to disk
    png_bytes: bytes = buff.getvalue()
    buff.close()
    print("converting data to png")
    return png_bytes

@celery_app.task(name="DOWNLOAD PNG IMAGE FROM REDIS INSTANCE")
def get_png_image(png_bytes):
    new_image = Image.open(BytesIO(png_bytes), format='png')
    # new_image.save("OUTPUT.png")
    print("new image to send", new_image)
    return new_image

