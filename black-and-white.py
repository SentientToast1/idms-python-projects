from PIL import Image

ORIGINALIMAGE = "img.jpeg"

OUTPUTIMAGE = "modifiedimg.jpg"



img = Image.open(ORIGINALIMAGE)
rgb_img = img.convert('RGB')
width, height = rgb_img.size
imgMod = Image.new('RGB',(width,height),color = (0,0,0))


for i in range(height):
    for j in range(width):
       r, g, b =  rgb_img.getpixel((j,i))
       avg = int((r + g + b)/3)
       imgMod.putpixel((j,i),(avg,avg,avg))

imgMod.save(OUTPUTIMAGE)