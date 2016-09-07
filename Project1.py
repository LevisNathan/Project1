from __future__ import print_function

from statistics import median

from PIL import Image

"""
Nathan K. Levis
Created in CST 205.
Takes pictures and puts parts of the images together
to make one coherent image.
"""
images = []
r = []  # these are arrays
g = []  # that hold the color
b = []  # values for each pixel
# the below makes sure that the picture is being added to the list
try:
    for x in range(1, 10):
        pic = Image.open("c:/Project1Images/" + str(x) + ".png")  # grabs the individual pictures
        images.append(pic)  # this adds the picture to the list

except():  # if the pictures are not added then the error below will display
    print("could not load Image")
final_pic = Image.new('RGB', (495, 557))  # creates a new image
final_pixel = final_pic.load()  # holds the pixel data for the save image

for l in range(0, 495):  # A nested loop to get the the position of the pixel.
    for w in range(0, 557):
        r.clear()
        g.clear()
        b.clear()
        for image in images:
            red, green, blue = image.getpixel((l, w))
            r.append(red)
            g.append(green)
            b.append(blue)

        temp = (int(median(r)), int(median(g)), int(median(b)))  # this is the temp to hold the median values
        final_pixel[l, w] = temp

final_pic.save("c:/Project1Images/Result.png")  # saves the pixel data


