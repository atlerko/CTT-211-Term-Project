from tkinter import *


def register():
    global register_screen
    global new_username
    global new_password
    global reg_user
    global reg_pass
    print("Registering")
    register_screen = Toplevel()
    register_screen.title("Register an Account")
    register_screen.geometry("400x300")

    new_username = StringVar()
    new_password = StringVar()

    Label(register_screen, text="Enter your new username and password", font=("Arial", 14)).pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Username:", font=("Arial", 20)).pack()
    reg_user = Entry(register_screen, textvariable=new_username)
    reg_user.pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Password:", font=("Arial", 20)).pack()
    reg_pass = Entry(register_screen, textvariable=new_password)
    reg_pass.pack()
    Label(register_screen, text="", font=("Arial", 20)).pack()
    Button(register_screen, text="Register", width=20, height=2, command=register_user).pack()


def register_user():
    file = open(new_username.get()+".txt", "w")
    file.write(new_username.get()+"\n")
    file.write(new_password.get())
    file.close()

    reg_user.delete(0, END)
    reg_pass.delete(0, END)

    Label(register_screen, text="Account Registered").pack()
