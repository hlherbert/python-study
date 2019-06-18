# transform normal jpeg to progressive jpeg

from PIL import Image
import os
import tkinter
import tkinter.filedialog

def seldir():
    dir = tkinter.filedialog.askdirectory()
    files = os.listdir(dir)
    fileList = []
    for f in files:
        filefullname = dir+'/'+f
        if (os.path.isdir(filefullname)):
            pass
        else:
            fileList.append(f)

    for f in fileList:
        filefullname = dir + '/' + f
        im = Image.open(filefullname)
        print("name:", filefullname)
        print("mode:", im.mode)
        newdir = dir + '-process'
        if not os.path.exists(newdir):
            os.mkdir(newdir)
        filenewname = newdir + '/' + f
        im.save(filenewname, "JPEG", quality = 80, optimize=True, progressive=True)
        print("name:", filenewname)
        print("mode:", im.mode)

root = tkinter.Tk()
btn = tkinter.Button(root, text="选择处理渐进JPEG的文件夹",command=seldir)
btn.pack()
root.mainloop()

