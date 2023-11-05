from PIL import Image


im = Image.open("/home/andrew/myprojects/Python/converter/api/assets/CW_Galen_Trollbane.blp")

im_png = im.save("output.png")