""""
I will test here if i can do a recursive of tthe function


print()
print("Welcome to the Shop Cart!")
print("Here is the menu!")
print("1.Review the Shop Cart 2.Add an item 3.Delete an item 4.Leave")
decision = input("Enter the option selected: ")
print(f"Your selected option was {decision}")
y_n = input("Y/N?:" ).capitalize

if y_n == "Y":
    print("a")
    #continue with the options
else:
    print
"""

def dance():

    while True:
        decision = input("Enter the option selected: ")

        if decision == "1":
            print("Decision 1")
            
        elif decision == "2":
            print("Decision 2")
        elif decision =="3":
            print("Decision 3")
        elif decision =="Leave":
            print("Decision leaving")
            False
        else:
            print("Error bro")

dance()