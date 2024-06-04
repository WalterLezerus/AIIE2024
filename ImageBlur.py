from PIL import Image
import random

filename = "newnewCAT.png"
catimage = Image.open(filename)
catimage.thumbnail((250,250))
for i in range(10):
    newimage = Image.new("RGB",catimage.size)
    for x in range(catimage.size[0]):
        for y in range(catimage.size[1]):
            color5 = catimage.getpixel((x,y))

            if x == 0 or y == catimage.size[1]-1:
                color1 = color5
            else:
                color1 = catimage.getpixel((x-1,y+1))

            if y == catimage.size[1]-1:
                color2 = color5
            else:
                color2 = catimage.getpixel((x,y+1))

            if x == catimage.size[0]-1 or y == catimage.size[1]-1:
                color3 = color5
            else:
                color3 = catimage.getpixel((x+1,y+1))

            if x == 0:
                color4 = color5
            else:
                color4 = catimage.getpixel((x-1,y))

            if x == catimage.size[0]-1:
                color6 = color5
            else:
                color6 = catimage.getpixel((x+1,y))

            if x == 0 or y == 0:
                color7 = color5
            else:
                color7 = catimage.getpixel((x-1,y-1))

            if y == 0:
                color8 = color5
            else:
                color8 = catimage.getpixel((x,y-1))

            if x == catimage.size[0]-1 or y == 0:
                color9 = color5
            else:
                color9 = catimage.getpixel((x+1,y-1))

            red = int((color1[0]+color2[0]+color3[0]+color4[0]+color5[0]+color6[0]+color7[0]+color8[0]+color9[0])/9)
            green = int((color1[1]+color2[1]+color3[1]+color4[1]+color5[1]+color6[1]+color7[1]+color8[1]+color9[1])/9)
            blue = int((color1[2]+color2[2]+color3[2]+color4[2]+color5[2]+color6[2]+color7[2]+color8[2]+color9[2])/9)

            newimage.putpixel((x,y),(red,green,blue))
    catimage = newimage

newimage.save("new"+filename)
#newimage.show()