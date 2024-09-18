"""Take the practice Patient Record Script and add authentication (user should be prompted for username and password BEFORE being able to see the case list).
The "database" with the usernames/passwords MUST be inside a dictionary.
The user is able to add or remove users from the dictionary.
After authenticating, the user is able to add or remove cases."""

auth = {
    "Carlos":"1234",
    "Pedro":"2345",
    "Juan":"1234",
    "Raul":"2345",
    "Rodrigo":"1234",
    "Paul":"2345",
    "Christian":"1234",
    "Pascal":"2345",
}

def caseRecord():

    while True:    

        print("Please enter your authentication info")
        username = input("Enter your Username: ").capitalize()
        password = input("Enter your Password: ")

        """if username in auth.keys() and password in auth.values():
            print(f"Welcome {username}!")
            print("Authentification Success!")"""
        #here i tried tuples to use the items built in function for dictionaries, and match key and value at the same time

        

        if (username,password) in auth.items():
            print(f"Welcome {username}!")
            print("Authentification Success!")

            while True:
                print("Menu")
                opt = input("A.Add user B.Remove C.Leave:  ").capitalize()


                if opt == "A": 
                    NewUser  = input("Enter the New User: ")
                    NewPass  = input("Enter the Password: ") 
                    
                    auth.update({NewUser:NewPass})
                    print(f"The updated Cases's List is {auth}")
                elif opt== "B":
                    print(f"The Cases's List is {auth}")
                    keyU = input("Enter the User to Remove: ").capitalize()
                    auth.pop(keyU)
                    print(f"The new Cases's List is {auth}")

                elif opt== "B":
                    break
                else:
                    print("There is an error!")
        
        else:
                print("Information not Valid!")


caseRecord()