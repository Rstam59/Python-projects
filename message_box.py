from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()


# showinfo,showwarning,showerror,askquestion, askokcancel, askyesno
def popup():
    messagebox.askokcancel("error", "Error 404 Not found")


my_button = Button(root, text="Hello", command=popup).pack()

root.mainloop()
