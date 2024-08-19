
"""Ask the user to input a number.
Check if the number is positive or negative
If it is positive, output pair if the number is pair and odd if the number is odd.
If it is negative, output a message saying that the number is negative."""



Active = True

while Active:
    number = float(input('Enter a number: '))
    if number < 0:
        print(f'{number} is negative number, please enter a positive number')
    else:
        if number % 2 == 0:
            print (f'The number {number} is pair')
            Active = False
        else:
            print(f'the number {number} is odd')
            Active = False

print('You have exit the app')