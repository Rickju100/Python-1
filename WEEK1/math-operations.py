#def the functions for operations
#create a menu to select the option for the operation
#show a message when you use 0 in divide

def addition(a,b):
    return a+b

def substraction (a,b):
    return a-b

def multiplication(a,b):
    return a*b 

def division(a,b):
    return a/b 

#make a loop with an menu panel

active = True
while active:
    menu = input('Choose an option from the menu. 1.Addition 2.Substraction 3.Multiplication 4. Division 5.Exit: ')
    if menu in ["1","2","3","4"]: #doing iteration allows the system to not lose time in process that are not needed
        value1 = int(input('Entry value 1: '))
        value2 = int(input('Entry value 2: '))
    
    if menu == "1":
        addtional = addition(value1,value2)
        print(f'The addition of {value1} plus {value2} is: {addtional}')
    elif menu == "2":
        subst = substraction(value1,value2)
        print(f'The substraction of {value1} minus {value2} is: {subst}')
    elif menu == "3":
        mul = multiplication(value1,value2)
        print(f'The multiplication of {value1} and {value2} is: {mul}')
    elif menu == "4":
        if value1 == 0:
            print('You can not divide by zero')
        elif value2 == 0:
            print('You can not divide by zero')
        else:
            div = division(value1,value2)
            print(f'The division betwen {value1} and {value2} is: {div}')
    elif menu == "5":
        print('You have left the menu')
        active = False
    else:
        print("Select a valid option")

print('Thanks for using our app, have a good day!')
