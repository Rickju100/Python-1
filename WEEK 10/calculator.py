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

#Here i declare the math operation functions with 2 parameters
def adddition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
