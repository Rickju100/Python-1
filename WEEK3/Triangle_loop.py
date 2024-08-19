


ACTIVE = True

while ACTIVE == True:    
    number = int(input("Enter the desire number: "))

    if number <= 0:
        print(f"{number} is not a valid number.")
        print("Please enter a valid number.")
    else:
        for i in range(1,number+1):
            print("*" * i)
        ACTIVE = False