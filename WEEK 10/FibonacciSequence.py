"""Write a Python function that takes a positive integer n and returns the n'th number of the Fibonacci sequence.
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers, starting from 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Use recursion to perform this task."""

def fibo (n):
    if n  in [1,2]:
        return 1
    else: 
        return (fibo(n-1) + fibo(n-2))

number = int(input("Enter a number: "))
for i in range(1,number):
    print(fibo(i))

#Ask to the teacher if i write number inside the fibo, and input 10, it will print 55
"""number = int(input("Enter a number: "))
for i in range(1,number):
    print(fibo(number))"""






