from tkinter import *

# Actual window
window = Tk()

# Test widget
myLabel = Label(window, text="Hello world!")

# Shoving on screen
myLabel.pack()
window.mainloop()