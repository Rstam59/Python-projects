from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="C:/User/hp/Desktop/WhatsApp Images",
                                           title="i hope it is gonna work",
                                           filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
my_img = ImageTk.PhotoImage(Image.open(root.filename))
ans = messagebox.askquestion("confirmation", "would you like to see that image")
if ans == "yes":
    my_label = Label(root, image=my_img).pack()
root.mainloop()
