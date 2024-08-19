
"""First_Name = input("Whats your name?: ").capitalize()
Last_Name = input("Whats your last name?: ").capitalize()
Age = int(input("Whats you age?: "))

DOB = 2024 - Age"""

#In this code i implement try and except, thinking about the scenario where the user did not input a number
try:
    First_Name = input("Whats your name?: ").capitalize()
    Last_Name = input("Whats your last name?: ").capitalize()
    Age = int(input("Whats you age?: "))

    if Age < 0: #This first conditional is to valid positive values only
            print(f"{Age} is negative number. Please enter a positive value")
    else:
        DOB = 2024 - Age
        #Here for the second conditional, i make a nesting for if. elif and else, to set some new argument rules and scenarios

        if 1940 <= DOB <= 1965:
                print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and your Generation is Baby Boomer")
        elif 1966 <= DOB <= 1980:
                print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and your Generation is Generation X")
        elif 1981 <= DOB <= 1996:
                print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and your Generation is Millenials")
        elif 1997 <= DOB <= 2012:
                print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and your Generation is Generation Z")
        elif 2013 <= DOB:
            print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and you are Too young!")  
        else: #This scenario is considering any number value outside the rules/ arguments above
                print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and you have no Generation Demographic")

except ValueError as ve:
        print(f"The value {Age} is not valid. Please enter a valid value. Error code info: {ve}")

            