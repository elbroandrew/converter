from PIL import Image
from io import BytesIO
from flask import g
from celeryapp.celery_worker import celery_app
import time


# im = Image.open("api/assets/CW_Galen_Trollbane.blp")

# im_png = im.save("converter/results/output.png")
@celery_app.task(name="CONVERTING IMAGE INTO .PNG TASK")
def save_img_bytes_to_redis(img_bytes: BytesIO):
    # g.redis_client.set('img', img_bytes.getvalue())
    print(img_bytes.getvalue())
    print("CONVERTING IMAGE BLP TO BYTES_IO")
    time.sleep(4)
    return "Hello from task"


def save_img_to_bytes(img_bytes: str) -> bytes:
    im = Image.open(img_bytes)
    buf = BytesIO()
    im.save(buf, format=im.format)  # save to buffer, not disk
    byte_im: bytes = buf.getvalue()
    return byte_im


def bytes_to_image(byte_im: bytes):
    new_image = Image.open(BytesIO(byte_im))
    new_image.save("OUTPUT.png")

