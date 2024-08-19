def validation(a,b):
    if username ==  user and password == passw:
        return True #I thought it was better to use the return here, to keep using the funcition after with some different prints over the code
    else: #I set up some rules for when one of the values is correct and the other is not, however, code can be writen better using the match and case coding options
        if username ==  user and password != passw:
            print(f"{name}, your password is Incorrect!")
        elif username != user and password == passw:
            print(f"{name}, your username is Incorrect!")
        else:
            print(f"{name}, the username and password are Incorrect!")
        return False #This return false is not needed, the code can work, but is not a good practice to skip it, is a explicit return, can make the code fail after and create more unnecesary troubles


#database
user = "Edward"
passw = "123123"


Active = True #Since i have only 2 posible values and dont need the loop to go many times, only in 2 scenarions, is better to use the boolean 

while Active:
    name = input("Whats your name?: ").capitalize() #This variable is not needed, but here is used for the f-string
    username = input("Enter the username: ") #is better not use capitalize here, and make the code caps sensitive, since this is confidential and sensitive informaiton, it should be enter correctly
    password = input("Enter the password: ")

    if validation(username,password) == True: #here is the validation of the boolean that is in the main function set up
        print(f"Hello {name}, the validation has been  Successful.")
        Active = False #Always remember to set up the activation of the loop and change it, or the loop will never end
    else:
        print("Enter valid information")

