"""Create a script that asks the user for five numbers.
The script should be able to tell which are the three highest numbers.
This script MUST contain at least one list.
Extras:
The script should print the sum of all numbers.
The code should also multiply all numbers and print the result."""

print("Please Enter 5 numbers")


list = []
count = 0
multiply = 1

while count < 5:
    number = int(input("Enter a number: "))
    list.append(number)
    count += 1 

sumatoria = sum(list)
print(f"The sum of the numbers of the list is: {sumatoria}")


for i in list:
    multiply *= i

print(f"The multiplication of {list} is {multiply}")