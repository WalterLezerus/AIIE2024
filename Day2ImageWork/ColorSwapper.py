from PIL import Image

filename = "CAT.png"
catimage = Image.open(filename)
catimage.thumbnail((250,250))

newimage = Image.new("RGB",catimage.size)

for x in range(catimage.size[0]):
    for y in range(catimage.size[1]):
        color = catimage.getpixel((x,y))
        newimage.putpixel((x,y),(color[2],color[1],color[0]))

newimage.save("swapped"+filename)