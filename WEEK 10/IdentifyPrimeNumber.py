"""Write a Python function that takes a number as a parameter and checks if the number is prime or not. 
Print the number if the number is prime, or print "this number is not prime" if it is not.
Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself."""

prime = int(input("Enter a number: "))

if prime > 1:
    for i in range (2, (prime//2)+1):
        if (prime % i) == 0:
            print(f"{prime}Is not a prime Number")
            break
    else:
        print(f"{prime} is a prime number")
else:
     print(f"{prime}Is not a prime Number")