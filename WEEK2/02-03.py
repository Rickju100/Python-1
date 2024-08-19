"""Create a script that asks the user if he wants to convert inch -> cm or cm -> inch.
The script should convert from inch -> cm or cm -> inch depending on the user's request.
The user will input the distance to convert.
Note: There are 2.54 cm in 1 inch and 0.39 inches in 1 cm"""


Active = True

while Active:
    menu = input("Chose an option from the menu to convert. 1-inch->cm. 2-cm->inch. 3-Exit: ")
        
    if menu == "1":
            distance = float(input("What is the distance to convert?: "))
            print(distance / 0.39 )
    elif menu == "2":
            distance = float(input("What is the distance to convert?: "))
            print(distance / 2.54 )
    elif menu == "3":
            print("Exit the app")
            Active = False

    else:
        print("Select a valid option")

print("Thanks for using the app")


    
