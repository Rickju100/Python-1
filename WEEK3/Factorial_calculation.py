"""The factorial of a number n is the product of all numbers less than or equal that n but greater or equal to 1.
ie. 2! ( 1 * 2 ) = 2,  3! (1 * 2 * 3) = 6.....
Create a script that asks for a number and prints its factorial on screen.
Use while loop, plus all you have learned so far.
Example Expected Output: 
Sample input: Enter a number: 4
Sample output: 4! = 24
"""\


contador = 1
ACTIVE = True

while ACTIVE == True:
    factorial = int(input("Enter the number: "))
    if factorial < 0:
        print("Value is not correct")
    elif factorial == 0:
        print("Factorial = 1")
    else:
        for i in range (1, factorial+1):
            contador *= i#print(contador) this print inside will print every value of i, from beginning to end, cause is every update of i
            ACTIVE = False

print(contador) #this print will only give the last value of contador