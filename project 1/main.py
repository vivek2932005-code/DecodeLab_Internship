My_Task = []


def registered():

    if len(My_Task) == 0:
        print("No Task Available")

    else:
        print("\nYour Tasks :- ")

        for index, task in enumerate(My_Task, start=1):
            print(f"{index}. {task}")


def notregistered():

    while True:

        task = input("Enter your Task (Type 'no' to stop):- ")

        if task.lower() == "no":
            break

        My_Task.append(task)

    print("Task Added Successfully")


while True:

    print("\n TO DO LIST ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Exit")

    check = int(input("Enter your choice :- "))

    if check == 1:
        notregistered()

    elif check == 2:
        registered()

    elif check == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")