from PIL import Image
from io import BytesIO
import redis


# im = Image.open("api/assets/CW_Galen_Trollbane.blp")

# im_png = im.save("converter/results/output.png")


def img_to_bytes(self, img_path: str) -> bytes:
    im = Image.open(img_path)
    # im_resize = im.resize((500, 500))
    buf = BytesIO()
    # im_resize.save(buf, format=im.format)
    im.save(buf, format=im.format)  # save to buffer, not disk
    byte_im: bytes = buf.getvalue()
    return byte_im


def bytes_to_image(self, byte_im: bytes):
    new_image = Image.open(BytesIO(byte_im))
    new_image.save("OUTPUT.png")

