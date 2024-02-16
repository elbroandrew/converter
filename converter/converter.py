from PIL import Image
from io import BytesIO
import redis
from flask import g
from time import sleep
# from celery import shared_task
from celeryapp.celery_worker import celery_app

#redis_client = redis.Redis(host='localhost', port=6379, decode_responses=False)  #  TODO: change to 'True' after testing image



# im = Image.open("api/assets/CW_Galen_Trollbane.blp")

# im_png = im.save("converter/results/output.png")
@celery_app.task(name="CONVERTING IMAGE INTO .PNG TASK")
def save_img_bytes_to_redis(img_bytes):
    # g.redis_client.set('img', img_bytes.getvalue())
    # redis_client.set("foo", "barr")
    sleep(3)
    print("hello")


def save_img_to_bytes(self, img_bytes: str) -> bytes:
    im = Image.open(img_bytes)
    # im_resize = im.resize((500, 500))
    buf = BytesIO()
    # im_resize.save(buf, format=im.format)
    im.save(buf, format=im.format)  # save to buffer, not disk
    byte_im: bytes = buf.getvalue()
    return byte_im


def bytes_to_image(self, byte_im: bytes):
    new_image = Image.open(BytesIO(byte_im))
    new_image.save("OUTPUT.png")

