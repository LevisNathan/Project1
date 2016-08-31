from __future__ import print_function

from statistics import median

from PIL import Image

images = []
val = [10, 6, 10, 6, 6, 6, 45]
print(median(val))

# the below makes sure that the picture is being added to the list
try:
    for x in range(1, 10):
        pic = Image.open("c:/Project1Images/" + str(x) + ".png")  # grabs the individual pictures
        images.append(pic)  # this adds the picture to the list
        pix = pic.load()  # holds the pixel values
        print(pic)
except():  # if the pictures are not added then the error below will display
    print("could not load Image")

rgb_IM = pic.convert('RGB')
r,g,b = rgb_IM.getpixel((1,1))

print("Hello")