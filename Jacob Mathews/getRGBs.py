from PIL import Image
import numpy


im = Image.open('image.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())

pixelsBin = ""
for tuple in pixel_values:
    for pixel in tuple:
        pixelsBin += str(bin(pixel))[2:].zfill(8)

#print pixel_values

print pixelsBin
