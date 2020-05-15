from PIL import Image
from sys import stdin

binaryPixels = stdin.read().rstrip("\n")

im = Image.open('image.png')
width, height = im.size
pixel_values = list(im.getdata())


rgbVals = []
i=0
while (i<len(binaryPixels)):
    byte = binaryPixels[i:i+8]
    byte = "0b" + byte
    byte = int(byte,2)
    if (byte > 0):
        byte = 255
    rgbVals.append(byte)
    i+=8


count = 0
for r in range(height):
    for c in range(width):
        im.putpixel((c,r), (rgbVals[count], rgbVals[count+1], rgbVals[count+2]))
        count += 3


im.save("newimage.png")
