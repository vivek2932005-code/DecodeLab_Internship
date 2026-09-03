total = 0


def addexpense():

    global total

    while True:

        expense = input("Enter Expense Amount (Type 'no' to stop) :- ")

        if expense.lower() == "no":
            break

        total = total + float(expense)

    print("Expense Added Successfully")


def viewexpense():

    print(f"\nTotal Spent :- ₹{total}")


while True:

    print("\n EXPENSE TRACKER ")
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. Exit")

    check = int(input("Enter your choice :- "))

    if check == 1:

        addexpense()

    elif check == 2:

        viewexpense()

    elif check == 3:

        print("Thank You")
        break

    else:

        print("Invalid Choice")