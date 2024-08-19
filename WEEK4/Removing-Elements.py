
"""Write a Python program to print a specified list after removing the 1st, 4th and 5th elements.
Use a while loop to fill the list with user inputs. The user may enter as many items as they want.
elements needed for the list to have 5 elements. 
Example Expected Output:
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Output : ['Green', 'White', 'Yellow']"""

colors = []

def inp_Color(): #I consider a best practice to define the function, since i will need to use it if the len condition for less than 4 elements is true, is also possible to not create a function and inside the while loop use the if conditional for when is less than 4 elements, but for me, is good practice
    while True:
        color = input("Enter a color: ").capitalize()
        colors.append(color)

        if color == "Exit":
            break
inp_Color() #here im calling the function to be executed!!
colors.remove("Exit") #For me is important to set this remove as a rule, to avoid printing the exit in the list

if len(colors) < 3: #This rule will set up an specific print if the list has no enough elements, less than 4
    print("We need more elements. We need at least 6")
    print(f"The list of elements is {colors}")
    inp_Color()


print(colors) #This will print the original color list

if len(colors) >= 8 : #This rule will set up an specific print if the list has no enough elements, less than 4   
    colors.remove(colors[4]) #remmove is better from the last to the first
    colors.remove(colors[3])
    colors.remove(colors[0])
    print(colors)
           
else:
    print(colors) #This will print the color list without element 1st,4th and 5th