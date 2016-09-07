from __future__ import print_function

from statistics import median

from PIL import Image

images = []
r = []
g = []
b = []


# the below makes sure that the picture is being added to the list
try:
    for x in range(1, 10):
        pic = Image.open("c:/Project1Images/" + str(x) + ".png")  # grabs the individual pictures
        images.append(pic)  # this adds the picture to the list
        pix = pic.load()  # holds the pixel values
except():  # if the pictures are not added then the error below will display
    print("could not load Image")
for x in range(1, 10):
    rgb_IM = images[x].convert('RGB')

    for l in range(0, 495):
        for w in range(0, 557):
            r, g, b = rgb_IM.getpixel((l, w))

            print(median(r[x]))
            print(median(g[x]))
            print(median(b[x]))
