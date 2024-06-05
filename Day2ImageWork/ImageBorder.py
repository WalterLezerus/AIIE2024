from PIL import Image

#opens the file (Have the Day2 Folder as the opened one)
filename = "CAT.png"
catimage = Image.open(filename)
catimage.thumbnail((250,250))

#Create a new image data
newimage = Image.new("RGB",catimage.size)

#Iterates the x axis
for x in range(catimage.size[0]):
    #iterates the y axis
    for y in range(catimage.size[1]):
        #Gets the color of any given pixel
        color = catimage.getpixel((x,y))
        #If the position of the pixels is within 15 pixels of the border it will make the pixels black
        if x <= 15 or x >= catimage.size[0]-15 or y <= 15 or y >= catimage.size[1]-15:
            newimage.putpixel((x,y),(0,0,0))
        #Otherwise it will print the original color
        else:
            newimage.putpixel((x,y),color)

#Saves to a new file
newimage.save("bordered"+filename)