from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import sqlite3

root=Tk()
root.geometry("400x400")
#creating connect
con=sqlite3.connect(("SO far i have.db"))
#creating cursor
cur=con.cursor()
#commit
con.commit()
#execute
#cur.execute('''CREATE TABLE ADRES(
#                    first_name text,
#                    second_name text
#            )''')

def sumbit():
    # creating connect
    con = sqlite3.connect(("SO far i have.db"))
    # creating cursor
    cur = con.cursor()
    cur.execute("INSERT INTO ADRES VALUES (:f_name,:s_name)",
                {
                    "f_name":f_name.get(),
                    "s_name":s_name.get()
                })
    # commit
    f_name.delete(0, END)
    s_name.delete(0, END)
    con.commit()
    con.close()

def query():
    # creating connect
    con = sqlite3.connect(("SO far i have.db"))
    # creating cursor
    cur = con.cursor()
    cur.execute("SELECT *,oid FROM ADRES")
    cur.fetchall()
    print(cur.fetchall())
    con.commit()
    con.close()
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1)
s_name=Entry(root,width=30)
s_name.grid(row=1,column=1)

#LAbels
f_label=Label(root,text="first name")
f_label.grid(row=0,column=0)
s_label=Label(root,text="second name")
s_label.grid(row=1,column=0)
#button
smb_button=Button(root,text="add record to database",command=sumbit)
smb_button.grid(row=2,column=0,padx=10,pady=10,columnspan=2,ipadx=100)
query_btn=Button(root,text="show records",command=query)
query_btn.grid(row=3,column=0,columnspan=2,ipadx=127,padx=10,pady=10)
#close connection
con.close()
root.mainloop()









#names=StringVar()
#names.set("rustam")
#drop=OptionMenu(root,names,"rustam",'rustem',"and others")
#drop.pack()
#label=Label(root,text=names.get())
#label.pack()