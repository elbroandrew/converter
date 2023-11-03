from PIL import Image
import PIL

im = Image.open("assets\HighElfWarMage.blp")

im_png = im.save("results\output.png")
