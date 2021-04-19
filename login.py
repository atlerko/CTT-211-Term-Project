#-------- Coded by Jining Zhao -------#

from goals import *
import os
from main_page import *


def login():
    global login_screen
    global username
    global password
    global log_user
    global log_pass
    print("Logging in")
    login_screen = Toplevel()
    login_screen.title("Login an Account")
    login_screen.geometry("400x300")

    username = StringVar()
    password = StringVar()

    Label(login_screen, text="Enter your username and password", font=("Arial", 14)).pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username:", font=("Arial", 20)).pack()
    log_user = Entry(login_screen, textvariable=username)
    log_user.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password:", font=("Arial", 20)).pack()
    log_pass = Entry(login_screen, textvariable=password)
    log_pass.pack()
    Label(login_screen, text="", font=("Arial", 20)).pack()
    Button(login_screen, text="Login", width=20, height=2, command=login_user).pack()


def login_user():
    test_user = username.get()
    test_pass = password.get()
    log_user.delete(0, END)
    log_pass.delete(0, END)

    account_list = os.listdir()

    if test_user+".txt" in account_list:
        file = open(test_user+".txt", "r")
        text = file.read().splitlines()
        if test_pass == text[1]:
            print("Logged in")
            main_page(test_user)
            ##################################################################
            #                                                                #
            # User has correctly logged in, display the main window here !!! #
            #                                                                #
            ##################################################################
            login_screen.destroy()
        else:
            print("Incorrect Password")
    else:
        print("No matching username")
