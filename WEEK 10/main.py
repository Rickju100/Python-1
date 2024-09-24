"""Create a Python module called calculator with the following specifications:
Inside the module define a function for each basic math operation (+, -, *, /).
Each function must receive 2 numbers as parameters and return the result of the operations.
Create another module called main with the following specifications:
Import the calculator module to the main module and create a menu.
The menu will have an option for each basic math operation and an option to exit.
Ask the user for the 2 numbers and call the corresponding function from calculator to calculate the result.
Create a dictionary that will keep a record of all calculations performed. The structure of the dictionary should be type_of_calculation: result. E.g: "Sum": 20
The dictionary should be updated with each calculation and the complete record must be displayed once the user decides to Exit the program.
The code must keep showing the main menu until the users chooses the Exit option."""

#Here i will have the menu, to call the functions from calculator
import calculator as cal #Import the calculator moddule

def main():
    print(f" \n Here is the menu") #Here i use  \n to start with an empty line, instead of print an empty print
    print("1.Addition 2.Subtraction 3.Multiplicatiton 4.Division 5.Exit ")

    while True: 
        menu = input("Enter the number for the option that you want to calculate: ")

        if menu == "1":
            a = int(input("Enter first value: "))
            b = int(input("Enter second value: "))
            print (cal.adddition(a,b))
        elif menu == "2":
            a = int(input("Enter first value: "))
            b = int(input("Enter second value: "))
            print (cal.subtraction(a,b))
        elif menu == "3":
            a = int(input("Enter first value: "))
            b = int(input("Enter second value: "))
            print (cal.multiplication(a,b))
        elif menu == "4":
            a = int(input("Enter first value: "))
            b = int(input("Enter second value: "))
            print (cal.division(a,b))
        elif menu == "5":
            print("Thanks for using the app! ")
            break
        else: 
            print("Select a valid option!")

main()