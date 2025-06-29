from PIL import Image
import src.paths as paths



def blackWhite(ogpath,outpath):
    img = Image.open(ogpath)
    rgb_img = img.convert('RGB')
    width, height = rgb_img.size
    imgMod = Image.new('RGB',(width,height),color = (0,0,0))


    for i in range(height):
        for j in range(width):
            r, g, b =  rgb_img.getpixel((j,i))
            avg = int((r + g + b)/3)
            imgMod.putpixel((j,i),(avg,avg,avg))

    imgMod.save(outpath)

blackWhite(paths.ORIGINALIMAGE,paths.OUTPUTIMAGE)