"""Create a script that asks the user to enter 10 numbers.
The code should add only the odd numbers to a list.
Repeated numbers should be added once.
Example Expected input:
[1,32,12,11,11, 7,8,9,9,7
Example Expected Output
Odd numbers are [1,11,7,9]"""

list = []
count = 0

while count < 10:
    number = int(input("Enter 10 numbers: "))
    if number % 2 != 0 and number not in list: # i when i set the rule add number "not in" makes the code avoid repeat numbers
        list.append(number)
    count += 1 #here if the count is inside the loop, it will continue, cause is never adding 1 counter


print(list)