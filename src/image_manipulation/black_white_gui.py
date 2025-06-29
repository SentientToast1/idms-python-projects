from tkinter import *
from tkinter import filedialog
from PIL import Image
import os
imgpath = ''
entered = ''
def openFile():
    global imgpath
    imgpath = filedialog.askopenfilename(filetypes=[
                                        ("JPG files","*.jpg"),
                                        ("PNG files","*.png"),
                                        ("JPEG files","*.jpeg")
                                   ])
    fileText.delete(0, END)
    fileText.insert(0, imgpath)
def nameCheck():
    global entered
    entered = outFile.get()
    if entered == '':
        default = os.path.splitext(os.path.basename(imgpath))[0]+ " modified"
        outFile.insert(0,default)
        entered = default
    outFile.config(state=DISABLED)
    submitName.config(state=DISABLED)
    fileText.config(state=DISABLED)
    browseButton.config(state=DISABLED)       
def converter():

    img = Image.open(imgpath)
    rgb_img = img.convert('RGB')
    width, height = rgb_img.size
    imgMod = Image.new('RGB',(width,height),color = (0,0,0))

    for i in range(height):
        for j in range(width):
            r, g, b =  rgb_img.getpixel((j,i))
            avg = int((r + g + b)/3)
            imgMod.putpixel((j,i),(avg,avg,avg))

    ogpath = os.path.dirname(imgpath)
    outpath = os.path.join(ogpath,f"{entered}.jpg")
    imgMod.save(outpath)

    fileText.config(state="normal")
    browseButton.config(state="normal")
    outFile.config(state="normal")
    submitName.config(state="normal")   
    outFile.delete(0,END)
    fileText.delete(0,END)

window = Tk()
window.geometry("400x240")
window.config(bg="#8B8B8B")
window.resizable(False,False)
window.title("Black and white converter")
icon = PhotoImage(file="icon.png")
window.iconphoto(True,icon)


fileText = Entry(window, width=25)
browseButton = Button(window, text="Browse...",command=openFile)
label = Label(window,text="Enter Output file name:")
outFile = Entry(window, width=25)
submitName = Button(window,text="Submit",command=nameCheck)
finalButton = Button(window,text="Change to Black and white!",command=converter)

fileText.pack(pady=15)
browseButton.pack(pady=5)
label.pack(pady=5)
outFile.pack(pady=5)
submitName.pack(pady=5)
finalButton.pack(pady=20)

window.mainloop()