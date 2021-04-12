from tkinter import *
from login import *


#GLOBAL VARS
INCOME_DICT = {}
EXPENSE_DICT = {}


def main_data_entry():
    global data_screen
    data_screen = Toplevel()
    data_screen.geometry("800x600")
    data_screen.title("Financial Goals")
    Label(data_screen, text="Income Entry", bg="white", width="100", height="2", font=("Arial", 12)).pack()

    Button(data_screen, text="Write Your Income", width=20, height=2, command=income_entry).pack()
    Button(data_screen, text="Delete Your Income", width=20, height=2, command=delete_income).pack()

    Button(data_screen, text="Write Your Expense", width=20, height=2, command=expense_entry).pack()
    Button(data_screen, text="Delete Your Expense", width=20, height=2, command=delete_expense).pack()

    Label(data_screen, text="Please click refresh after submiting.", font=("arial", 15), padx=2)
    Button(data_screen, text="Refresh", width=20, height=2, command=refresh).pack()

    Label(data_screen, text="Recent Entries", font=("arial", 15), padx=2)


def refresh():
    for key in INCOME_DICT:
        Label(data_screen, text=key, font=("arial", 15), padx=2).pack()
        for i in range(len(INCOME_DICT[key])):
            Label(data_screen, text=INCOME_DICT[key][i][0], font=("arial", 12), padx=2).pack()
            Label(data_screen, text=str(INCOME_DICT[key][i][1]), font=("arial", 12), padx=2).pack()

    for key in EXPENSE_DICT:
        Label(data_screen, text=key, font=("arial", 15), padx=2).pack()
        for i in range(len(EXPENSE_DICT[key])):
            Label(data_screen, text=EXPENSE_DICT[key][i][0], font=("arial", 8), padx=2).pack()
            Label(data_screen, text=str(EXPENSE_DICT[key][i][1]), font=("arial", 8), padx=2).pack()

def income_entry():
    global INCOME_AMOUNT
    global INCOME_NAME
    global INCOME_TYPE
    global income_screen

    INCOME_AMOUNT = StringVar()
    INCOME_NAME = StringVar()
    INCOME_TYPE = StringVar()

    income_screen = Toplevel()
    income_screen.geometry("600x400")
    income_screen.title("Write Your Income")

    Label(income_screen, text="Enter your income:", font=("Arial", 20)).pack()
    Label(income_screen, text="").pack()
    Label(income_screen, text="Income type:", font=("Arial", 20)).pack()
    income_t = Entry(income_screen, textvariable=INCOME_TYPE)
    income_t.pack()
    Label(income_screen, text="").pack()
    Label(income_screen, text="Description:", font=("Arial", 20)).pack()
    income_n = Entry(income_screen, textvariable=INCOME_NAME)
    income_n.pack()
    Label(income_screen, text="").pack()
    Label(income_screen, text="Enter the income amount:", font=("Arial", 20)).pack()
    income_a = Entry(income_screen, textvariable=INCOME_AMOUNT)
    income_a.pack()
    Label(income_screen, text="").pack()
    Button(income_screen, text="Save Income", width=20, height=2, command=save_income).pack()


def delete_income():
    global income_delete_screen
    income_delete_screen = Toplevel()
    income_delete_screen.geometry("600x400")
    income_delete_screen.title("Delete An Income")
    income_delete_file = StringVar()
    Label(income_delete_screen, text="Please, enter the name of the income you want to delete:", font=("Arial", 20)).pack()
    Label(income_delete_screen, text="").pack()
    Entry(income_delete_screen, textvariable=income_delete_file).pack()
    Label(income_delete_screen, text="").pack()
    Button(income_delete_screen, text="Delete Goal", width=20, height=2, command=delete).pack()


def save_income():
    if INCOME_TYPE.get() not in INCOME_DICT:
        INCOME_DICT[INCOME_TYPE.get()] = []
        INCOME_DICT[INCOME_TYPE.get()].append((INCOME_NAME.get(), int(INCOME_AMOUNT.get())))
    else:
        INCOME_DICT[INCOME_TYPE.get()].append((INCOME_NAME.get(), int(INCOME_AMOUNT.get())))
    income_screen.destroy()


def delete():
    i = ""
    if INCOME_TYPE.get() in INCOME_DICT:
        INCOME_DICT.pop(INCOME_TYPE.get())
        #print("Income deleted.", a[0][0].get(), a[0][1].get())
        i = "I"
    elif EXPENSE_TYPE.get() in EXPENSE_DICT:
        EXPENSE_DICT.pop(EXPENSE_TYPE.get())
        #print("Expense deleted.", a[0][0].get(), a[0][1].get())
        i = "E"
    else:
        new_screen = Toplevel()
        new_screen.geometry("300x200")
        new_screen.title("Error")
        Label(new_screen, text="This type of income or outcome does not exist").pack()
        Button(new_screen, text="Click here, to restart", width=20, height=10, command=delete_income).pack()
        print("This type of expense does not exist")
        # BUNA BAKKKKKK OLMADI BU AMA CALISIYO
       #new_screen.destroy()
    if i == "I":
        income_delete_screen.destroy()
    elif i == "E":
        expense_delete_screen.destroy()


def expense_entry():
    global expense_screen
    global EXPENSE_NAME
    global EXPENSE_TYPE
    global EXPENSE_AMOUNT

    EXPENSE_NAME = StringVar()
    EXPENSE_TYPE = StringVar()
    EXPENSE_AMOUNT = StringVar()

    expense_screen = Toplevel()
    expense_screen.geometry("600x400")
    expense_screen.title("Write Your Expense")

    Label(expense_screen, text="Enter your expense:", font=("Arial", 20)).pack()
    Label(expense_screen, text="").pack()
    Label(expense_screen, text="Expense type:", font=("Arial", 20)).pack()
    Entry(expense_screen, textvariable=EXPENSE_NAME).pack()
    Label(expense_screen, text="").pack()
    Label(expense_screen, text="Description:", font=("Arial", 20)).pack()
    Entry(expense_screen, textvariable=EXPENSE_TYPE).pack()
    Label(expense_screen, text="").pack()
    Label(expense_screen, text="Enter the expense amount:", font=("Arial", 20)).pack()
    Entry(expense_screen, textvariable=EXPENSE_AMOUNT).pack()
    Label(expense_screen, text="").pack()
    Button(expense_screen, text="Save Expense", width=20, height=2, command=save_expense).pack()


def delete_expense():
    global expense_delete_screen
    expense_delete_screen = Toplevel()
    expense_delete_screen.geometry("600x400")
    expense_delete_screen.title("Delete An Income")
    expense_delete_file = StringVar()
    Label(expense_delete_screen, text="Please, enter the name of the expense you want to delete:", font=("Arial", 20)).pack()
    Label(expense_delete_screen, text="").pack()
    Entry(expense_delete_screen, textvariable=expense_delete_file).pack()
    Label(expense_delete_screen, text="").pack()
    Button(expense_delete_screen, text="Delete Expense", width=20, height=2, command=delete).pack()


def save_expense():
    if EXPENSE_TYPE.get() not in EXPENSE_DICT:
        EXPENSE_DICT[EXPENSE_TYPE.get()] = []
        EXPENSE_DICT[EXPENSE_TYPE.get()].append((EXPENSE_NAME.get(), int(EXPENSE_AMOUNT.get())))
    else:
        EXPENSE_DICT[EXPENSE_TYPE.get()].append((EXPENSE_NAME.get(), int(EXPENSE_AMOUNT.get())))

    expense_screen.destroy()



