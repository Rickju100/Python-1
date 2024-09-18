import shopping_cart as SC 
import gspreading as gpr
import pandas as pd

"""This is the main code, i will use this file to make the request to the other py files.
Mostly i will try here to call the functions, and create the main loop for that"""

print()
print("Welcome to the Shop Cart!")
print("Here is the menu!")
print("1.Review the Store 2.Add a price 3.Delete an item 4.Review the list 5.Get the total to pay 6.Leave")

while True:
    decision = input("Enter the option selected: ")
    print(f"Your selected option was {decision}")
    print("Y for Yes, N for No")
    y_n = input("Y/N?: " ).capitalize()

    if y_n == "Y":
        print("hello")
        if decision == "1":
            gpr.get_data()
            data = pd.DataFrame(gpr.get_data())
            print(data)
        elif decision == "2":
            gpr.edit()
        elif decision == "3":
            gpr.clear()
        elif decision == "4":
            gpr.getCol(5)
        elif decision == "5":
            gpr.suma() #I can try to ask how much would like to pay and give the vuelto

    else:
        print("You Selected No!")
