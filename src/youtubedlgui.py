# Importing libraries (or I guess they're modules but shush)
from __future__ import unicode_literals
from tkinter import *
from youtube_dl import *
import requests
import os

# Main window
window = Tk()
window.geometry("480x180")
window.title("Youtube DLGUI")
window.resizable(0,0)

# Function for downloading the video
def convert():
    try:
        SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Desktop'

        ydl_opts = {
            'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url.get()])
        convertiondone()
    except Exception:
        errordialogue()

# Dialogue box that shows when a conversion is successful
def convertiondone():
    convertsuccess = Tk()
    convertsuccess.title("Downloaded!")
    convertsuccess.geometry("180x50")
    convertsuccess.resizable(0,0)
    converttext = Label(convertsuccess, text="Video downloaded!")
    convertok = Button(convertsuccess, text="OK", command=convertsuccess.destroy)
    converttext.pack()
    convertok.pack()

# Error dialogue that is spitted out when an error occurs, I'll try to add error handling later on
def errordialogue():
    errorwindow = Tk()
    errorwindow.title("Error!")
    errorwindow.geometry("180x50")
    errorwindow.resizable(0,0)
    errortext = Label(errorwindow, text="There was an error!")
    errorok = Button(errorwindow, text="OK", command=errorwindow.destroy)
    errortext.pack()
    errorok.pack()


# Widgets, idk
eobj = Label(window, text="   ")
logo = Label(window, text="Youtube DLGUI")
url = Entry(window)

clicked = StringVar()
clicked.set("MP4")
formatdrop = OptionMenu(window, clicked, "MP4", "MP3")
downloadbutton = Button(window, text="Convert & Download", command=convert)

# Shoving on screen

# firstclick and on_entry_click function stolen from StackOverflow: https://stackoverflow.com/questions/30491721/how-to-insert-a-temporary-text-in-a-tkinter-entry-widget
firstclick = True

def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""        
    global firstclick

    if firstclick: # if this is the first time they clicked it
        firstclick = False
        url.delete(0, "end") # delete all the text in the entry

logo.pack()

url.pack()
url.insert(0, "URL")
url.bind('<FocusIn>', on_entry_click)
formatdrop.pack()
downloadbutton.pack()


# Looping
window.mainloop()