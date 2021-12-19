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
        SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Desktop' # Path to video folder

        # Options for video if MP4 is selected
        if clicked.get() == "MP4":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
            }
        # Same but if MP3 is selected
        elif clicked.get() == "MP3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s'
            }
        # Downloading the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url.get()])
        convertiondone()

    # (Unproper) Error handling
    except Exception:
        exceptionerrordialogue()
    except SyntaxError:
        syntaxerrordialogue()

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

# Error dialogues (I'll do proper error handling one day)
def exceptionerrordialogue():
    errorwindow = Tk()
    errorwindow.title("Error!")
    errorwindow.geometry("180x50")
    errorwindow.resizable(0,0)
    errortext = Label(errorwindow, text="There was an error!")
    errorok = Button(errorwindow, text="OK", command=errorwindow.destroy)
    errortext.pack()
    errorok.pack()

def syntaxerrordialogue():
    syntaxerrorwindow = Tk()
    syntaxerrorwindow.title("Error!")
    syntaxerrorwindow.geometry("180x50")
    syntaxerrorwindow.resizable(0,0)
    syntaxtext = Label(syntaxerrorwindow, text="There was an error!\nSyntaxException")
    syntaxok = Button(syntaxerrorwindow, text="OK", command=syntaxerrorwindow.destroy)
    syntaxtext.pack()
    syntaxok.pack()

# Widgets, idk
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