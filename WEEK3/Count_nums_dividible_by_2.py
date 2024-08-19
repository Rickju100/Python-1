"""Create a script that asks the user for a number and print the count of all numbers that are divisible by 2 between that number and zero (include 0, but not the number).
Use while loop, plus all you have learned so far.
Example Expected Output:
Enter a number: 4
Sample output: Between 0 and 4 there are 2 numbers divisible by 2"""



count = 1
ACTIVE = True

while ACTIVE == True:
    number = int(input("Enter the number till you want to count: "))
    if number < 0:
        print(f"{number} is not a valid value.")
        print("Enter a valid value.")
    else: 
        while count <= number:
            if count % 2 == 0:
                print(count)
            count += 1
            ACTIVE = False
       
