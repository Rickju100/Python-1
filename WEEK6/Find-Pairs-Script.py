"""This program finds all pairs of numbers in a list that add up to a target number

Create a program that takes in a list of numbers and a target number.

The program should find all pairs of numbers in the list that add up to the target number

At the end print out the pairs.

Sample data:
numbers = [1, 2, 4, 6, 8, 10, 12, 13]
target = 14
Output:
[1, 13] [2, 12] [4, 10] [6, 8]"""

numbers = [1, 2, 4, 6, 8, 10, 12, 13]

numList = []
target = int(input("Target number: "))

#for the loop, the best way to get 2 values for the list is creating 2 looping as for, 1 for the first range to get the first value [i,0]
#The second range/loop will help me to get the second value, without repiting the first number so i+1, as [0,j]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target: #Always remeber i+j is not the same as numbers[i] + numbers[j], the first is every value in the loop, the other is every value in the list
            numList.append([numbers[i], numbers[j]]) #remeber to write it as [i,j], this will make the list save another list, other wise the system will print an error list.append() takes exactly one argument (2 given)

print(numList)
