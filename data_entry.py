#-------- Coded by Atil Erkoc -------#

from tkinter import *
from login import *


#GLOBAL VARS
INCOME_DICT = {}
EXPENSE_DICT = {}


def main_data_entry():
    global data_screen
    global income_label_frame
    global expense_label_frame
    global income_label
    global expense_label
    data_screen = Toplevel()
    data_screen.geometry("800x600")
    data_screen.title("Income, Expense Entry")
    Label(data_screen, text="Income / Expense Entry", bg="white", width="100", height="2", font=("Arial", 24)).pack()

    Button(data_screen, text="Write Your Income", width=20, height=2, command=income_entry).pack()
    Button(data_screen, text="Delete Your Income", width=20, height=2, command=delete_income).pack()

    Button(data_screen, text="Write Your Expense", width=20, height=2, command=expense_entry).pack()
    Button(data_screen, text="Delete Your Expense", width=20, height=2, command=delete_expense).pack()

    Label(data_screen, text="Please click refresh after submiting.", font=("arial", 15), padx=2)
    Button(data_screen, text="Refresh", width=20, height=2, command=refresh).pack()

    income_label_frame = LabelFrame(data_screen, bd=10, relief=RIDGE, padx=4, text="Recent Incomes", fg="darkblue", font=("Arial",30))
    income_label_frame.place(x=0, y=250, width=395, height=350)

    expense_label_frame = LabelFrame(data_screen, bd=10, relief=RIDGE, padx=4, text="Recent Expenses", fg="darkblue", font=("Arial",30))
    expense_label_frame.place(x=405, y=250, width=390, height=350)

    income_label = Label(income_label_frame, text="There is no income, create a new income and hit refresh", font=("Arial", 14))
    income_label.pack()
    expense_label = Label(expense_label_frame, text="There is no expense, create a new expense and hit refresh", font=("Arial", 14))
    expense_label.pack()


def refresh():
    for widget in income_label_frame.winfo_children():
        widget.destroy()

    for widget in expense_label_frame.winfo_children():
        widget.destroy()

    if INCOME_DICT != {}:
        for key in INCOME_DICT:
            income_type = Label(income_label_frame, text="Income Type: "+key, font=("arial", 15), padx=2)
            income_type.pack()
            for i in range(len(INCOME_DICT[key])):
                desc_label = Label(income_label_frame, text="Income Description: "+INCOME_DICT[key][i][0], font=("arial", 12), padx=2)
                desc_label.pack()
                amount_label = Label(income_label_frame, text="Amount: "+str(INCOME_DICT[key][i][1]), font=("arial", 12), padx=2)
                amount_label.pack()
    else:
        Label(income_label_frame, text="There is no income, create a new income and hit refresh", font=("Arial", 14)).pack()

    if EXPENSE_DICT != {}:
        for key in EXPENSE_DICT:
            expense_type = Label(expense_label_frame, text="Expense Type: "+key, font=("arial", 15), padx=2)
            expense_type.pack()
            for i in range(len(EXPENSE_DICT[key])):
                desc_label = Label(expense_label_frame, text="Expense Description: "+EXPENSE_DICT[key][i][0], font=("arial", 12), padx=2)
                desc_label.pack()
                amount_label = Label(expense_label_frame, text="Amount: "+str(EXPENSE_DICT[key][i][1]), font=("arial", 12), padx=2)
                amount_label.pack()
    else:
        Label(expense_label_frame, text="There is no expense, create a new expense and hit refresh", font=("Arial", 14)).pack()


def income_entry():
    global INCOME_AMOUNT
    global INCOME_NAME
    global INCOME_TYPE
    global income_screen

    income_screen = Toplevel()
    income_screen.geometry("600x400")
    income_screen.title("Write Your Income")

    INCOME_AMOUNT = StringVar()
    INCOME_NAME = StringVar()
    INCOME_TYPE = StringVar(income_screen)
    key_list = get_dict_keys(INCOME_DICT)

    Label(income_screen, text="Enter your income:", font=("Arial", 20)).pack()
    Label(income_screen, text="").pack()
    Label(income_screen, text="Income type:", font=("Arial", 20)).pack()
    income_t = Entry(income_screen, textvariable=INCOME_TYPE)
    income_t.pack()

    if key_list != []:
        Label(income_screen, text="").pack()
        Label(income_screen, text="Or, select from the following", font=("Arial", 20)).pack()
        key_dropdown = OptionMenu(income_screen, INCOME_TYPE, *key_list)
        key_dropdown.pack()

    Label(income_screen, text="Description:", font=("Arial", 20)).pack()
    income_n = Entry(income_screen, textvariable=INCOME_NAME)
    income_n.pack()
    Label(income_screen, text="").pack()
    Label(income_screen, text="Enter the income amount (only numerical values):", font=("Arial", 20)).pack()
    income_a = Entry(income_screen, textvariable=INCOME_AMOUNT)
    income_a.pack()
    Label(income_screen, text="").pack()
    Button(income_screen, text="Save Income", width=20, height=2, command=save_income).pack()


def delete_income():
    global income_delete_screen
    global income_delete_file
    global i_description_delete_file

    income_delete_screen = Toplevel()
    income_delete_screen.geometry("600x400")
    income_delete_screen.title("Delete An Income")
    income_delete_file = StringVar(income_delete_screen)
    i_description_delete_file = StringVar()
    key_list = get_dict_keys(INCOME_DICT)
    Label(income_delete_screen, text="Please, select the type of the income you want to delete:", font=("Arial", 20)).pack()
    Label(income_delete_screen, text="").pack()
    if INCOME_DICT:
        key_dropdown = OptionMenu(income_delete_screen, income_delete_file, *key_list)
        key_dropdown.pack()
        Button(income_delete_screen, text="Next", width=20, height=2, command=income_next_d).pack()
    else:
        Label(income_delete_screen, text="Please, enter an income to delete", font=("Arial", 20)).pack()


def income_next_d():
    Label(income_delete_screen, text="").pack()
    Label(income_delete_screen, text="Choose the income description you want to delete", font=("Arial", 20)).pack()
    desc_list = get_description_list(INCOME_DICT, income_delete_file.get())
    description_delete_option = OptionMenu(income_delete_screen, i_description_delete_file, *desc_list)
    description_delete_option.pack()
    Button(income_delete_screen, text="Next", width=20, height=2, command=income_next_b).pack()


def income_next_b():
    Button(income_delete_screen, text="Delete Income", width=20, height=2, command=delete_i).pack()


def save_income():
    if INCOME_TYPE.get() not in INCOME_DICT:
        INCOME_DICT[INCOME_TYPE.get()] = []
        INCOME_DICT[INCOME_TYPE.get()].append((INCOME_NAME.get(), int(INCOME_AMOUNT.get())))
    else:
        INCOME_DICT[INCOME_TYPE.get()].append((INCOME_NAME.get(), int(INCOME_AMOUNT.get())))
    income_screen.destroy()


def delete_i():
    key = income_delete_file.get()
    desc = i_description_delete_file.get()
    if key in INCOME_DICT:
        for i in range(len(INCOME_DICT[key])):
            if desc.split(":")[0] == INCOME_DICT[key][i][0]:
                INCOME_DICT[key].remove((INCOME_DICT[key][i]))
                break

    if INCOME_DICT[key] == [] :
        INCOME_DICT.pop(key)
    income_delete_screen.destroy()


def expense_entry():
    global expense_screen
    global EXPENSE_NAME
    global EXPENSE_TYPE
    global EXPENSE_AMOUNT

    EXPENSE_NAME = StringVar()
    EXPENSE_TYPE = StringVar()
    EXPENSE_AMOUNT = StringVar()
    key_list = get_dict_keys(EXPENSE_DICT)

    expense_screen = Toplevel()
    expense_screen.geometry("600x400")
    expense_screen.title("Write Your Expense")

    Label(expense_screen, text="Enter your expense:", font=("Arial", 20)).pack()
    Label(expense_screen, text="").pack()
    Label(expense_screen, text="Expense type:", font=("Arial", 20)).pack()
    Entry(expense_screen, textvariable=EXPENSE_TYPE).pack()

    if key_list != []:
        Label(expense_screen, text="").pack()
        Label(expense_screen, text="Or, select from the following", font=("Arial", 20)).pack()
        key_dropdown = OptionMenu(expense_screen, EXPENSE_TYPE, *key_list)
        key_dropdown.pack()

    Label(expense_screen, text="").pack()
    Label(expense_screen, text="Description:", font=("Arial", 20)).pack()
    Entry(expense_screen, textvariable=EXPENSE_NAME).pack()
    Label(expense_screen, text="").pack()
    Label(expense_screen, text="Enter the expense amount:", font=("Arial", 20)).pack()
    Entry(expense_screen, textvariable=EXPENSE_AMOUNT).pack()
    Label(expense_screen, text="").pack()
    Button(expense_screen, text="Save Expense", width=20, height=2, command=save_expense).pack()


def delete_expense():
    global expense_delete_screen
    global expense_delete_file
    global e_description_delete_file
    expense_delete_screen = Toplevel()
    expense_delete_screen.geometry("600x400")
    expense_delete_screen.title("Delete An Income")
    expense_delete_file = StringVar(expense_delete_screen)
    e_description_delete_file = StringVar()
    key_list = get_dict_keys(EXPENSE_DICT)
    Label(expense_delete_screen, text="Please, select the type of the income you want to delete:", font=("Arial", 20)).pack()
    Label(expense_delete_screen, text="").pack()
    if EXPENSE_DICT:
        key_dropdown = OptionMenu(expense_delete_screen, expense_delete_file, *key_list)
        key_dropdown.pack()
        Button(expense_delete_screen, text="Next", width=20, height=2, command=expense_next_d).pack()
    else:
        Label(expense_delete_screen, text="Please, enter an expense to delete", font=("Arial", 20)).pack()


def expense_next_d():
    Label(expense_delete_screen, text="").pack()
    Label(expense_delete_screen, text="Choose the expense description you want to delete", font=("Arial", 20)).pack()
    desc_list = get_description_list(EXPENSE_DICT, expense_delete_file.get())
    description_delete_option = OptionMenu(expense_delete_screen, e_description_delete_file, *desc_list)
    description_delete_option.pack()
    Button(expense_delete_screen, text="Next", width=20, height=2, command=expense_next_b).pack()


def expense_next_b():
    Button(expense_delete_screen, text="Delete Expense", width=20, height=2, command=delete_e).pack()


def delete_e():
    key = expense_delete_file.get()
    desc = e_description_delete_file.get()
    if key in EXPENSE_DICT:
        for i in range(len(EXPENSE_DICT[key])):
            if desc.split(":")[0] == EXPENSE_DICT[key][i][0]:
                EXPENSE_DICT[key].remove((EXPENSE_DICT[key][i]))
                break

    if EXPENSE_DICT[key] == []:
        EXPENSE_DICT.pop(key)

    expense_delete_screen.destroy()

def save_expense():
    if EXPENSE_TYPE.get() not in EXPENSE_DICT:
        EXPENSE_DICT[EXPENSE_TYPE.get()] = []
        EXPENSE_DICT[EXPENSE_TYPE.get()].append((EXPENSE_NAME.get(), int(EXPENSE_AMOUNT.get())))
    else:
        EXPENSE_DICT[EXPENSE_TYPE.get()].append((EXPENSE_NAME.get(), int(EXPENSE_AMOUNT.get())))

    expense_screen.destroy()


def get_dict_keys(dit):
    key_list = []
    for key in dit.keys():
        key_list.append(key)
    return key_list


def get_description_list(dit, key):
    description_list = []
    for i in range(len(dit[key])):
        description_list.append(dit[key][i][0] + ": $" + str(dit[key][i][1]))
    return description_list
