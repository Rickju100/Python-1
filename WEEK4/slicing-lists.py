"""Create a script that prints the last 4 elements in a list.
Use a while to fill the list with user inputs. The user can add as many elements as they want.
If the list's length is less than 4 the program should print This list is too short."""

list = []

while True: #I used true here because it will always keeps active and dont need to count
    elements = input("Enter an element to the list or Exit: ").capitalize()
    list.append(elements)
    
    if elements == "Exit":
        break

list.remove("Exit")

if len(list) < 4:
    print("Alert!")
    print("This list is too short.")
else:
    print(list[-4:])



