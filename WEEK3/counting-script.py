
"""Create a script that counts up to a certain number.

Ask the user to input a number higher than 0.
The script will then count from 1 up to that number.
The user will be asked if they want to count again or if they want to exit the program."""

start_number = int(input("Enter a number higher than 0: "))


active = 0
count = 1

while count <= start_number:
    if start_number > 0:
        print(count)
        count +=  1
        question = input("Want to continue counting? 1.Yes 2.No: ")
        if question == "1":
            repeat = int(input("Enter a number higher than 0: "))
            count += 1
            
        else:
            break
    else:
        break
        

print(count)   

