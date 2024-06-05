from PIL import Image
import os

filename = "CAT.png"
catimage = Image.open(filename)
catimage.thumbnail((250,250))

newimage = Image.new("RGB",catimage.size)

for x in range(catimage.size[0]):
    for y in range(catimage.size[1]):
        color = catimage.getpixel((x,y))
        if x <= 15 or x >= catimage.size[0]-15 or y <= 15 or y >= catimage.size[1]-15:
            newimage.putpixel((x,y),(0,0,0))
        else:
            newimage.putpixel((x,y),color)

newimage.save("bordered"+filename)