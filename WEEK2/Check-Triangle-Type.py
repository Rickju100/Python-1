"""Write a Python program to check a triangle is equilateral, isosceles or scalene.
Ask the user for the measures of each side.
Note:
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides."""


"""
x = float(input("Enter x side: "))
y = float(input("Enter y side: "))
z = float(input("Enter z side: "))"""

Active = True

while Active:
    #I prefer to use float, considering if the user enter a decimal value
    x = float(input("Enter x side: "))
    y = float(input("Enter y side: "))
    z = float(input("Enter z side: "))

    if x == 0 or y == 0 or z == 0: #Always remember i can use as many or / and as i wish. 
        #remember x or y or z== 0, is not the same than x == 0 or y == 0 or z == 0. In the fist only z is equal to 0 and the machine read it that way
        print("Zero is not a valid value.")
    else:
        if x == y  == z:
            print("The triangle is equilateral")
        elif x == y or y == z or x == z:
            print("The triangle is isosceles")
        else:
            print("The triangle is scalene")
        Active = False
print("Thanks for using our app")
