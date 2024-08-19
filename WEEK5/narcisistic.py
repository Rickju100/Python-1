"""Create a script that checks if a number is narcissistic.
**A narcissistic number is a positive number which is the sum of its own digits, each raised to the power of the number of digits.
For example: 153 is a narcissistic number because 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
Other examples to test your code are 370, 407 or 9474
The script should ask the user for an input and print a message advising whether the number is narcissistic or not.
Only numbers higher than 0 should be checked."""

number = int(input("Enter a number: "))
numeros = len(str(number))

for i in str(number):
    mult = int(i)**int(numeros) #In here i want the new variable to have the multiplication of every value of i and the len of the number

    if mult == number:
        print("The numbner is narcissistic")
    else:
        print(f"{number} is not narcissistic")