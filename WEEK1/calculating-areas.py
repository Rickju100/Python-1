
#Areas functions

def area_circle():
    r = int(input("Input the radio: "))
    r2 = r ** 2
    pi = 3.14159 
    print(r2*pi)
def area_square ():
    a = int(input("Input side a: "))
    b = int(input("Input side b: "))
    print(a*b)

def area_triangle ():
    a = int(input("Input base: "))
    b = int(input("Input height: "))
    print ((a*b)/2)

def area_sphere():
    r = int(input("Input the radio: "))
    r2 = r ** 2
    pi = 3.14159 
    print((pi * r2)*4)

active = True #True activation is better always, instead of a number, cause is a condition

while active:
    #i always prefer to make a menu, can work on inprove the menu
    menu = input('Select an option from the menu of areas. 1.Circle 2.Square 2.Triangle 4.Sphere 5.Exit: ' )
    if menu == "1":
        area_circle()
    elif menu == "2":
        area_square()
    elif menu == "3":
        area_triangle()
    elif menu == "4":
        area_sphere()
    elif menu == "5":
        print("You are leaving the app now")
        active = False
    else:
        print('Select a valid option')
print('Thanks for using our app')
