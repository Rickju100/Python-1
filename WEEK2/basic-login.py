def validation():
    if username ==  user and password == passw:
        return True #I thought it was better to use the return here, to keep using the funcition after with some different prints over the code
    else:
        print("Fail")

#database
user = "Edward"
passw = "123123"


Active = True #Since i have only 2 posible values and dont need the loop to go many times, only in 2 scenarions, is better to use the boolean 

while Active:
    name = input("Whats your name?: ").capitalize() #This variable is not needed, but here is used for the f-string
    username = input("Enter the username: ") #is better not use capitalize here, and make the code caps sensitive, since this is confidential and sensitive informaiton, it should be enter correctly
    password = input("Enter the password: ")

    if validation() == True: #here is the validation of the boolean that is in the main function set up
        print(f"Hello {name}, the validation has been  Succesfully")
        Active = False #Always remember to set up the activation of the loop and change it, or the loop will never end
    else:
        print("Enter valid information")

