"""Create a script that takes the following data as input:
First name.
Last name.
Age.
Once the user enters the data, your script should output the user's full name and the year he/she was born.
In addition, depending on the year of birth the script should also print the corresponding Generation Demographic:
If the person was born between 1940 and 1965: Baby Boomer.
From 1966 to 1980: Generation X.
From 1981 to 1996: Millenials.
From 1997 to 2012: Generation Z.
2013 or after: Too young!"""

"""Active = True
while Active:"""

First_Name = input("Whats your name?: ").capitalize()
Last_Name = input("Whats your last name?: ").capitalize()
Age = int(input("Whats you age?: "))

DOB = 2024 - Age

if Age < 0:
        print(f"{Age} is negative number. Please enter a positive value")
elif Age == str:
        print(f"{Age} is not a validvalue. Please enter a valid value")
else:
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
    else:
            print(f"Hello {First_Name} {Last_Name}, you were born in {DOB} and you have no Generation Demographic")