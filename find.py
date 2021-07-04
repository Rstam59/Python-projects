from tkinter import *

root = Tk()
root.title("greeting")
e = Entry(root, borderwidth=10,columnspawn=2)
e.grid(row=0,column=3)
e.insert(0,"i mean here")


def clicked_button():
    lab = Label(root, text="hi "+e.get()+" how are you", fg="blue")
    lab.grid(row=0,column=0)
def bye():
    lab1 = Label(root, text="bye "+e.get()+" cya", fg="blue")
    lab1.grid(row=1, column=1)


myButton = Button(root, text="enter your name here!", command=clicked_button, padx=15, pady=15, fg="red", bg="black").grid(row=0,column=0)
myButton = Button(root, text="im gonna miss you", command=bye, padx=15, pady=15, fg="red", bg="black").grid(row=0,column=1)

root.mainloop()
