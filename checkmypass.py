import requests
import hashlib
import sys
from tkinter import *

root = Tk()
ent = Entry(root, width=23)
ent.grid(row=0, column=0, columnspan=4)
def button_click():
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, (str(current)))

button_1 = Button(root, text="press for searching", padx=30, pady=15, command=lambda: button_click())

button_1.grid(column=0, row=1)
root.mainloop()


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching {res.status_code}"," check the api and try again")
    return res
def get_password_leaks_count(hashes,tail):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == tail:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char, tail = sha1_password[:5], sha1_password[5:]
    print(first_5char,tail)
    response = request_api_data(first_5char)#read_response(request_api_data((first_5char)
    return get_password_leaks_count(response, tail)


def main(password):
    count = pwned_api_check(password)
    if count:
        print(f"{password} was found {count} times you should change your password")
    else:
        print(f"{password} was not found.Carry on")

my_password = input("enter you password: ")
if __name__ == "__main__":
    main(my_password)
