from tkinter import *

root = Tk()
ent = Entry(root, width=23)
ent.grid(row=0, column=0, columnspan=4)


# functions
def button_click(num):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, (str(current) + str(num)))


def cleaner():
    ent.delete(0, END)


def add():
    first_number = ent.get()
    global f_num
    global math
    math = "+"
    f_num = int(first_number)
    ent.delete(0, END)


def subtract():
    first_number = ent.get()
    global f_num
    global math
    math = "-"
    f_num = int(first_number)
    ent.delete(0, END)


def multiply():
    first_number = ent.get()
    global f_num
    global math
    math = "*"
    f_num = float(first_number)
    ent.delete(0, END)


def divide():
    first_number = ent.get()
    global f_num
    global math
    math = "/"
    f_num = int(first_number)
    ent.delete(0, END)


def answer():
    ans = int(ent.get())
    ent.delete(0, END)
    if math == "+":
        ent.insert(0, (f_num + ans))
    elif math == "-":
        ent.insert(0, (f_num - ans))
    elif math == "*":
        ent.insert(0, (f_num * ans))
    elif math == "/":
        ent.insert(0, (f_num / ans))


# define buttons
button_1 = Button(root, text="1", padx=10, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=10, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=10, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=10, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=10, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=10, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=10, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=10, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=10, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=10, pady=10, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=26, pady=10, command=add)
button_sub = Button(root, text="-", padx=10, pady=10, command=subtract)
button_divide = Button(root, text="/", padx=10, pady=10, command=divide)
button_multiply = Button(root, text="*", padx=10, pady=10, command=multiply)
button_clear = Button(root, text="Clear", padx=17, pady=10, command=cleaner)
button_equal = Button(root, text="=", padx=27, pady=10, command=answer)
# put the button on the screen
button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)

button_0.grid(column=0, row=4, )
button_add.grid(column=1, row=4, columnspan=2)
button_clear.grid(column=0, row=5, columnspan=2)
button_equal.grid(column=2, row=5, columnspan=2)
button_sub.grid(column=3, row=1)
button_divide.grid(column=3, row=2)
button_multiply.grid(column=3, row=3)

root.mainloop()
