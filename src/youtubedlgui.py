# Importing libraries (or I guess they're modules but shush)
from __future__ import unicode_literals
from tkinter import *
from youtube_dl import *
import requests
import os

# Main window
window = Tk()
window.geometry("480x380")
window.title("Youtube DLGUI")
window.resizable(0,0)

# Functions
def convert():
    SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Desktop'

    ydl_opts = {
        'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url.get()])
    convertiondone()

def convertiondone():
    convertsuccess = Tk()
    convertsuccess.title("Downloaded!")
    convertsuccess.resizable(0,0)
    converttext = Label(convertsuccess, text="Video downloaded!")
    convertok = Button(convertsuccess, text="OK", command=convertsuccess.destroy)
    converttext.pack()
    convertok.pack()

def errordialogue():
    errorwindow = Tk()
    errorwindow.title("Error!")
    errorwindow.resizable(0,0)
    errortext = Label(errorwindow, text="There was an error!")
    errorok = Button(errorwindow, text="OK", command=errorwindow.destroy)
    errortext.pack()
    errorok.pack()


# Widgets, idk
eobj = Label(window, text="   ")
logo = Label(window, text="Youtube DLGUI")
downloadbutton = Button(window, text="Convert & Download", command=convert)
url = Entry(window)

# Shoving on screen
eobj.grid(row=0, column=0, columnspan=10)
logo.grid(row=0, column=11)

eobj.grid(row=1, column=0, columnspan=10)
url.grid(row=1, column=11)

eobj.grid(row=2, column=0, columnspan=10)
downloadbutton.grid(row=2, column=0)

# Looping
window.mainloop()