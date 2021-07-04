from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image")
# images
my_img = ImageTk.PhotoImage(Image.open("WhatsApp Images/debat.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open('WhatsApp Images/xan bagi.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('WhatsApp Images/IMG-20180327-WA0002.jpg'))

li = [my_img, my_img1, my_img2]
global current_image
# noinspection PyRedeclaration
current_image = 0


# functions
def to_forward():
    global current_image
    global my_label
    my_label.grid_forget()
    temp = current_image + 1
    status = Label(root, text="image " + str(temp) + " of " + str(len(li)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    if current_image <= len(li) - 2:
        my_label = Label(root, image=li[current_image + 1])
        my_label.grid(row=1, column=0, columnspan=3)
        current_image += 1
    else:
        current_image = 0
        my_label = Label(root, image=li[0])
        my_label.grid(row=1, column=0, columnspan=3)


def to_back():
    global current_image
    global my_label
    status = Label(root, text="image " + str(temp) + " of " + str(len(li)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
    my_label.grid_forget()
    if current_image >= (len(li) - 2) * (-1):
        my_label = Label(root, image=li[current_image - 1])
        my_label.grid(row=1, column=0, columnspan=3)
        current_image -= 1
    else:
        current_image = 0
        my_label = Label(root, image=li[0])
        my_label.grid(row=1, column=0, columnspan=3)


status = Label(root, text="image " + str(current_image) + " of " + str(len(li)), bd=1, relief=SUNKEN, anchor=E)
# buttons
forward_button = Button(root, text=">>", command=to_forward)
forward_button.grid(row=0, column=2)
back_button = Button(root, text="<<", command=to_back, )
back_button.grid(row=0, column=0)
# display
button_quit = Button(root, text="exit", command=root.quit, padx=30, pady=10)
button_quit.grid(row=0, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)
my_label = Label(root, image=my_img)
my_label.grid(row=1, column=0, columnspan=3)
# state=DISABLED
root.mainloop()
