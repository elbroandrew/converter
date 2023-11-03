from PIL import Image

im = Image.open("api\\assets\\CW_Galen_Trollbane.blp")

im_png = im.save("api\\results\\output.png")
