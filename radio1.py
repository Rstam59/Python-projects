from tkinter import *
from tkinter import Tk

from PIL import ImageTk, Image

root: Tk = Tk()
programming = StringVar()
programming.set(value="Python")

Languages = ["Python", "c", "Java", "C++", "Javascript"]
for language in Languages:
    Radiobutton(root, text=language, variable=programming, value=language).pack(anchor=W)


def displayer(value):
    Label(root, text=value).pack()


my_button = Button(root, text="Click me", command=lambda: displayer(programming.get()))
my_button.pack()

root.mainloop()
