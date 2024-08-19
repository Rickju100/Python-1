
print("Hello, Welcome to the pair/odd app. Enjoy!") #This print is first and out from the loop, to make an unique welcome

Active = True

while Active:

    try: #I used try and except, considering the scenario of user input a value different from a numer
        number = float(input('Enter a number: ')) #I prefer to use float instead of int considering different user inputs scenarios

        if number < 0:
            print(f'{number} is negative number, please enter a positive number')
        else:
            if number % 2 == 0:
                print (f'The number {number} is pair')
            else:
                print(f'the number {number} is odd')
            Active = False
          

    except ValueError as ve: #Here the as ve is not really needed, but is importat for printing the error in the print message
        #I preffered to write 3 prints to have a better message in term of importance for customer
        print("ERROR!",end="\n") # the end is not needed here, just for practice
        print(f"The input is not a number. Enter a valid value.") 
        print(f"Review code. Code error: {ve}.")

print('You have exit the app')