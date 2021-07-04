import re
with open("test/i_wanna_see", mode="a") as my_file:
    text =input("enter your email address ")
    pasword_text = input("enter your password: ")
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    password_pattern = re.compile("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")
    password_c = password_pattern.fullmatch(pasword_text)
    c = pattern.fullmatch(text)
    if c and password_c:
        adder = (my_file.write(text+"-"+pasword_text+""))
        print("your email is saved")
    else:
        print("invalid email address")