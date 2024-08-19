
"""Create a script that counts up to a certain number.

Ask the user to input a number higher than 0.
The script will then count from 1 up to that number.
The user will be asked if they want to count again or if they want to exit the program."""


def contando():
    count = 1
    Active = True

    while Active == True:
        max_number = int(input("Enter a number higher than 0: "))
        if max_number > 0:
            while count <= max_number:
                print(count)
                count += 1
            question = input("Would you like to contiunue Y/N: ").capitalize()
            if question == "N":
                print("Thanks for using the app!")
                Active = False
            else:
                count = 1

        else:
            print("Enter a valid value")

contando()
