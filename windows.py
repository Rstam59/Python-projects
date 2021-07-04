from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title('Hey it is mee')


def second_window():
    global my_img
    top = Toplevel()
    button_2 = Button(top, text="close window", command=top.destroy).pack(anchor=W)
    my_img = ImageTk.PhotoImage(Image.open("WhatsApp Images/IMG-20190423-WA0001.jpg"))
    lbl = Label(top, image=my_img)
    lbl.pack()




btn=Button(root,text="click if you need second window",command=second_window).pack()


root.mainloop()