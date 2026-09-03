import random
import string


def generatepassword():

    length = int(input("Enter Password Length :- "))

    characters = string.ascii_letters + string.digits

    password = ""

    for i in range(length):

        password = password + random.choice(characters)

    print(f"\nGenerated Password :- {password}")


while True:

    print("\n PASSWORD GENERATOR ")
    print("1. Generate Password")
    print("2. Exit")

    check = int(input("Enter your choice :- "))

    if check == 1:

        generatepassword()

    elif check == 2:

        print("Thank You")
        break

    else:

        print("Invalid Choice")