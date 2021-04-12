from tkinter import *
from login import *
import os


def goals(user):
    global goal_screen
    global filename
    global username
    global goal_label

    username = user
    goal_screen = Toplevel()
    goal_screen.geometry("800x600")
    goal_screen.title("Financial Goals")
    Label(goal_screen, text=username+"'s Financial Goals", bg="white", width="100", height="2", font=("Arial", 16)).pack()

    Bframe = Frame(goal_screen)
    Bframe.pack(side=TOP)
    Button(Bframe, text="Create Goal", width=20, height=2, command=create_goal).pack(side=LEFT)
    Button(Bframe, text="Delete Goals", width=20, height=2, command=delete_goal).pack(side=RIGHT)
    Button(Bframe, text="Refresh Goals", width=20, height=2, command=refresh).pack()

    Label(goal_screen, text="Current Balance: "+"$", width="100", height="2", font=("Arial", 16)).pack()

    #
    # Add the variable for the user's current balance between 'Current Balance: ' and '$'
    #
    # Should look like: text="Current Balance: "+ MONEY_VARIABLE + "$"
    #

    account_list = os.listdir()
    if username + "goals.txt" in account_list:
        file = open(username + "goals.txt", "r")
        text = file.read()
        goal_label = Label(goal_screen, text=text, font=("Arial", 14))
        goal_label.pack()
    else:
        goal_label = Label(goal_screen, text="No current goals, create a new goal and hit refresh", font=("Arial", 14))
        goal_label.pack()


def refresh():
    account_list = os.listdir()
    if username + "goals.txt" in account_list:
        file = open(username + "goals.txt", "r")
        text = file.read()
        goal_label.config(text=text)
    else:
        goal_label.config(text="")


def create_goal():
    global create_screen
    global goal_name
    global goal_desc
    create_screen = Toplevel()
    create_screen.geometry("400x300")
    create_screen.title("Create a new Goal")
    goal_name = StringVar()
    goal_desc = StringVar()

    Label(create_screen, text="Enter a new financial goal:", font=("Arial", 20)).pack()
    Label(create_screen, text="").pack()
    Label(create_screen, text="Goal name:", font=("Arial", 20)).pack()
    Entry(create_screen, textvariable=goal_name).pack()
    Label(create_screen, text="").pack()
    Label(create_screen, text="Money Amount:", font=("Arial", 20)).pack()
    Entry(create_screen, textvariable=goal_desc).pack()
    Label(create_screen, text="").pack()
    Button(create_screen, text="Save Goal", width=20, height=2, command=save_goal).pack()


def delete_goal():
    if os.path.exists(username+"goals.txt"):
        os.remove(username+"goals.txt")
    else:
        print("Goal does not exist")


def save_goal():
    file = open(username+"goals.txt", "a")
    file.write(goal_name.get() + "\n")
    file.write(goal_desc.get() + "$" + "\n")
    file.close()
    create_screen.destroy()
