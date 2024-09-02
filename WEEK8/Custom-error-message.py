"""Create a script that displays a custom error message depending on the user's selection.
The message should use the template below, which should be stored as an f-string in a variable:
------------------------------------------
Error while executing task {number selected by user}
Error Number: {custom error number}
Message:  {custom error message}
------------------------------------------
The options and messages available to the user are:
1-> Error: 404, Message: Not Found
2-> Error: 500, Message: Internal Server Error
3-> Error: 418, Message: I'm a teapot
4-> No Error, Message: "SUCCESS"""

print()
print("Select an option from the menu")
print("Menu Options 1,2,3,4")

option = input("Select the option: ")

options_tuple = ("404", "Not Found!", "500", "Internal Server Error!", "418", "I'm a teapot!", "SUCCESS!" )

print()
if option == "1":
    print(f"Error while executing task {option}\n Error Number: {options_tuple[0]}\n Message:  {options_tuple[1]}\n")
#i can write all the code with th \n to divide it into new lines, and it will  make no issue
elif option == "2":
    print(f"Error while executing task {option}\n" f"Error Number: {options_tuple[2]}\n" f"Message:  {options_tuple[3]}\n")
#I can also write different fstrings in the same print, individually
elif option == "3":
    print(f"Error while executing task {option}\n" f"Error Number: {options_tuple[4]}\n" f"Message:  {options_tuple[5]}\n")

elif option == "4":
    print( f"Message:  {options_tuple[6]}\n")

else:
    print("Buy a new pc!")

print()