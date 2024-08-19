"""Write a Python program that prints the elements in a list in reverse.
Use a while loop to get the elements of the list.
Example Expected Output: 
list1 = ['this', 'is',  'a', 'sentence']
Expected output:
sentence a is this"""

list = []
count = 0

while count < 5:
    elements = input("Enter an element: ")
    list.append(elements)
    count += 1
    
list.reverse()    
print(list)

