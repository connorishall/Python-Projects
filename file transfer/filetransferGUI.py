import tkinter as tk
from tkinter import filedialog
import os
import datetime
from datetime import timedelta
from tkinter import messagebox

txt_browser1 = tk.Entry(text='',width=70)
txt_browser1.grid(row=0,column=2,rowspan=1,columnspan=1,padx=(30,40),pady=(40,0))
txt_browser2 = tk.Entry(text='',width=70)
txt_browser2.grid(row=1,column=2,rowspan=1,columnspan=1,padx=(30,40),pady=(0,0))


#Browse, check for file, and close program buttons 
btn_add = tk.Button(width=12,height=1,text='Browse..',command = lambda: getSource())
btn_add.grid(row=0,column=1,padx=(5,0),pady=(40,0))
btn_add = tk.Button(width=12,height=1,text='Browse..',command = lambda: getDestination())
btn_add.grid(row=1,column=1,padx=(5,0),pady=(5,0))
btn_add = tk.Button(width=12,height=2,text='Check for files...',command = lambda: moveFiles())
btn_add.grid(row=2,column=1,padx=(5,0),pady=(5,0))
btn_add = tk.Button(width=12,height=2,text='Close Program',command = lambda: closeGUI())
btn_add.grid(row=2,column=2,padx=(5,0),pady=(5,0))



#Function to get the source file 
def getSource():
    path = filedialog.askdirectory()
    print (txt_browser1.insert(tk.INSERT,path))

#Function to choose where to file should be sent to
def getDestination():
    path = filedialog.askdirectory()
    print (txt_browser2.insert(tk.INSERT,path))

#Move file function
def moveFiles():
    source = txt_browser1.get()
    destination = txt_browser2.get()
    files = os.listdir(source)
#Loop that determines if a file was modified within the last 24 hours
    for i in files:
        abspath = os.path.join(source,i)
        modeTime = os.path.getmtime(abspath)
        modificationTime = datetime.datetime.fromtimestamp(modeTime)
        twentyfour = datetime.datetime.now() - datetime.timedelta(hours = 24)
        if modificationTime > twentyfour:
            shutil.move(abspath, destination)
            print("Your file was moved!")
        else:
            print("Files were not modified within 24 hours.")

#Close gui function
def closeGUI():
    if messagebox.askokcancel("Exit Program","Ok to exit application?"):
        os._exit(0)
