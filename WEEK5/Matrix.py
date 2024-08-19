"""Create a square matrix (3x3, for example) by using a list of lists.
Ask the user to input 9 numbers to fill the matrix.
Print the matrix by using nested for loops.
Example Expected Output:
list = [ [3,4,5] , [3,2,1], [7,8,9]]
Output:
3 4 5
3 2 1
7 8 9"""
#Here i prefer to create individual list that after will be included in the Lista General, because im not sure how to do it other way
Lista1 = []
Lista2 = []
Lista3 = []

Lista_General= [Lista1, Lista2, Lista3] #I preffer to make the array this way with all the other list, in order to iterate over then in the print


print("Please enter 9 numbers!")

for i in range(9):
    a = int(input("Enter a number: ")) #I use a, cause i always try a letter when i test a variable, and did not change it due to time, but can be named any other name, example "number", "input" , etc...
    if i < 3: #This will make all values when i is less than than 3 to be append, remeber always, it start counting from 0
        Lista1.append(a)
    elif i< 6:
        Lista2.append(a)
    else:
        Lista3.append(a)
      
#There should be a better way to print this, but in order to set up as it was required for the task, i was only able to print it this way
print(Lista_General[0])
print(Lista_General[1])
print(Lista_General[2])