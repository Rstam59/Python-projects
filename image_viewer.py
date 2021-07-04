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
current_image=0


# functions
def to_forward():
    global current_image
    global my_label
    my_label.grid_forget()
    if current_image <= len(li)-2:
        my_label = Label(root, image=li[current_image + 1])
        my_label.grid(row=1, column=0, columnspan=3)
        current_image += 1
    else:
        current_image=0
        my_label=Label(root,image=li[0])
        my_label.grid(row=1, column=0, columnspan=3)



def to_back(i):
    global current_image
    global my_label
    my_label.grid_forget()
    if current_image >= (len(li) - 2)*(-1):
        my_label = Label(root, image=li[current_image - 1])
        my_label.grid(row=1, column=0, columnspan=3)
        current_image -= 1
    else:
        current_image = 0
        my_label = Label(root, image=li[0])
        my_label.grid(row=1, column=0, columnspan=3)



# buttons
forward_button = Button(root, text=">>", command=lambda: to_forward())
forward_button.grid(row=0, column=2)
back_button = Button(root, text="<<", command=lambda: to_back(0))
back_button.grid(row=0, column=0)
# display
button_quit = Button(root, text="exit", command=root.quit, padx=30, pady=10)
button_quit.grid(row=0, column=1)

my_label = Label(root, image=my_img)
my_label.grid(row=1, column=0, columnspan=3)

root.mainloop()
