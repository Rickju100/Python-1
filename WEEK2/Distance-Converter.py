
Active = True
#I preffer to make a loop on here, to simulate if is a calculator for an user
while Active: 
    menu = input("Chose an option from the menu to convert. 1-inch->cm. 2-cm->inch. 3-Exit: ")
    if menu in ["1","2"]: #This first alone for the menu, is considering only the 2 first value, to save some non necesary process for the machine
        distance = int(input("What is the distance to convert?: "))

    if menu == "1":
        print(distance / 0.39 )
    elif menu == "2":
        print(distance / 2.54 )
    elif menu == "3":
        print("Exit the app")
        Active = False
    
    else:
        print("Select a valid option")

print("Thanks for using the app")