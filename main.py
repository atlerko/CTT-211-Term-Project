from register import *
from login import *


def main():
    global screen
    screen = Tk()
    screen.geometry("800x600")
    screen.title("Financial Program - To be named")
    Label(text="Financial Program - To be named", bg="white", width="100", height="2", font=("Arial", 12)).pack()
    Label(text="Created by Atil Erkoç and Jining Zhao", bg="white", width="100", height="2", font=("Arial", 12)).pack()
    Label(text="", font=("Arial", 100)).pack()
    Button(text="Login", width="20", height="3", font=("Arial", 12), command=login).pack()
    Label(text="", font=("Arial", 20)).pack()
    Button(text="Register", width="20", height="3", font=("Arial", 12), command=register).pack()

    screen.mainloop()


main()
