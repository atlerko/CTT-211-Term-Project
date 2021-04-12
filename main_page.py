from goals import *
from data_entry import *
import matplotlib.pyplot as plt


def main_page(loginuser):
    global income_results
    global expense_results
    global balance_results
    global username
    username = loginuser

    base_screen = Toplevel()
    base_screen.geometry("1200x500")
    base_screen.title("PIFY Personal Money Management System")
    label_title = Label(base_screen, text="PIFY Personal Money Management System", bd=15, relief=RIDGE,
                        bg="white", fg="darkblue", font=("Arial", 50), padx=2, pady=4)
    label_title.pack(side="top", fill="x")

    data_frame = Frame(base_screen, bd=15, relief=RIDGE, padx=10)
    data_frame.place(x=0, y=100, width=1200, height=350)

    left_label_frame = LabelFrame(data_frame, bd=10, relief=RIDGE, padx=4, text="Important Numbers", fg="darkblue", font=("Arial",30))
    left_label_frame.place(x=0, y=5, width=575, height=310)
    right_label_frame = LabelFrame(data_frame, bd=10, relief=RIDGE, padx=4, text="Usefull Graphs", fg="darkblue", font=("Arial",30))
    right_label_frame.place(x=585, y=5,  width=570, height=310)

    b_frame = Frame(base_screen, bd=15, relief=RIDGE, padx=4)
    b_frame.place(x=0, y=450, width=1200, height=50)

    add_income_button = Button(b_frame, text="Add Income or Expense", font=("arial", 20), fg="darkblue", command=main_data_entry)
    add_income_button.grid(row=0, column=0)


    # fix the user thing ASAP
    add_goal_button = Button(b_frame, text="Goals", font=("arial", 20), fg="darkblue", command=username_helper)
    add_goal_button.grid(row=0, column=2)

    logout_button = Button(b_frame, text="Logout", font=("arial", 20), fg="darkblue", command=base_screen.destroy)
    logout_button.grid(row=0, column=6)

    exit_button = Button(b_frame, text="Exit", font=("arial", 20), fg="darkblue", command=quit)
    exit_button.grid(row=0, column=7)

    income_label = Label(left_label_frame, text="Your Total Income", font=("arial", 15), padx=2)
    income_label.grid(row=0, column=0)
    income_results = Label(left_label_frame, text="0",font=("arial", 15),  padx=2)

    income_results.grid(row=0, column=2)

    expense_label = Label(left_label_frame, text="Your Total Expense", font=("arial", 15), padx=2)
    expense_label.grid(row=1, column=0)
    expense_results = Label(left_label_frame, text="0", font=("arial", 15), padx=2)
    expense_results.grid(row=1, column=2)

    refresh_button = Button(left_label_frame, text="Refresh Page", command=refresh)
    refresh_button.grid(row=4, column=0)

    balance_label = Label(left_label_frame, text="Your Balance", font=("arial", 15), padx=2)
    balance_label.grid(row=2, column=0)
    balance_results = Label(left_label_frame, text="0", font=("arial", 15), padx=2)
    balance_results.grid(row=2, column=2)



    expense_g = Button(right_label_frame, text="Distribution of Your Expenses by Type", font=("arial", 20), padx=2, command=expense_graph)
    expense_g.grid(row=0, column=0)

    income_g = Button(right_label_frame, text="Distribution of Your Income by Type", font=("arial", 20), padx=2, command=income_graph)
    income_g.grid(row=3, column=0)

    income_expense_g = Button(right_label_frame, text="Proportion of your income to your Expense", font=("arial", 20), padx=2, command=income_expense_graph)
    income_expense_g.grid(row=6, column=0)


def refresh():
    total_income = 0
    total_expense = 0
    for key in INCOME_DICT:
        for i in range(len(INCOME_DICT[key])):
            total_income += INCOME_DICT[key][i][1]

    for key in EXPENSE_DICT:
        for i in range(len(EXPENSE_DICT[key])):
            total_expense += EXPENSE_DICT[key][i][1]

    income_results.configure(text=str(total_income))
    expense_results.config(text=str(total_expense))

    balance_results.config(text=str(total_income-total_expense))


def expense_graph():
    key_list = []
    value_list = []
    for key in EXPENSE_DICT:
        total_expense = 0
        key_list.append(key)
        for i in range(len(EXPENSE_DICT[key])):
            total_expense += EXPENSE_DICT[key][i][1]
        value_list.append(total_expense)

    plt.pie(value_list, labels=key_list, shadow=False, startangle=90)
    plt.show()


def income_graph():
    key_list = []
    value_list = []
    for key in INCOME_DICT:
        total_income = 0
        key_list.append(key)
        for i in range(len(INCOME_DICT[key])):
            total_income += INCOME_DICT[key][i][1]
        value_list.append(total_income)

    plt.pie(value_list, labels=key_list, shadow=False, startangle=90)
    plt.show()


def income_expense_graph():
    total_income = 0
    total_expense = 0
    for key in INCOME_DICT:
        for i in range(len(INCOME_DICT[key])):
            total_income += INCOME_DICT[key][i][1]

    for key in EXPENSE_DICT:
        for i in range(len(EXPENSE_DICT[key])):
            total_expense += EXPENSE_DICT[key][i][1]
    plt.pie([total_income, total_expense], labels=["Income", "Expense"], shadow=False, startangle=90)
    plt.show()


def username_helper():
    tempname = username
    goals(tempname)



