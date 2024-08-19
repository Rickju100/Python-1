
menu = input("Chose an option from the menu to convert. 1-inch->cm. 2-cm->inch. 3-Exit: ")
distance = int(input("What is the distance to convert?: "))
        
if menu == "1":
    print(distance / 0.39 )
elif menu == "2":
    print(distance / 2.54 )
elif menu == "3":
    print("Exit the app")
 
else:
    print("Select a valid option")
print("Thanks for using the app")