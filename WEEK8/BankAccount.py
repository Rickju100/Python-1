"""Create a script that simulates the bank account for a user.
The bank should follow the specifications below:
Ask for the user to input their initial balance.
The bank will then ask the user whether they want to make a deposit or a withdraw and ask for the amount.
The bank will save the history of all transactions and the respective amount.
Each transaction will be stored in a list, the elements of the list will be tuples composed of the type of transaction and the amount.
The initial balance will be updated accordingly with each transaction amount (Users could have a negative balance).
The bank will ask the user if they wish to make another transaction.
When the user decides to stop making transactions, the bank should print the initial balance, a summary of all the transactions and the current balance.
**Extra: 
Create a list that contains tuples with a user and password to authenticate an user before the program starts.
Have the program notify the user when their balance is 0 and prevent their balance to reach a negative amount."""



usertuple = ("Tony","Stark") #This tuple will store the full user information

while True: #I think is better to make this code a loop, due to the user and pass matching needed
    username = input("Enter the username: ").capitalize()
    password = input("Enter the password: ").capitalize()

    if username == usertuple[0] and password == usertuple[1]: #This simple conditional will allow to reviwe if input from user and tuple information match
        False
        transactions = []
        finalAmount = 0

        #I will use float for the fist int, because usually balance has decimal numbers
        iBalance = float(input("Enter your initial balance: "))

        while True:

            print("Do you want to make a deposit or a withdraw ?")
            DoW = input("1.Deposit 2.Withdraw 3.Leave: ").capitalize()

            if DoW =="Deposit":
                amount = float(input("Enter The amount: "))
                DoWtupple = (DoW,amount)
                transactions.append(DoWtupple)
                finalAmount += amount
            elif DoW == "Withdraw":
                amount = float(input("Enter The amount: "))
                DoWtupple = (DoW,amount)
                transactions.append(DoWtupple)
                finalAmount -= amount
            else:
                break

        
        lBalance = iBalance - finalAmount #LastBalance Calculation . I prefer to make this variable here to not create a problem into the while loop

        if lBalance == 0:
            print()
            print("Your balance is 0, prevent their balance to reach a negative amount!")

        else:
            print()
            print(f"Your initial balance was {iBalance}.")
            print(f"The transactions history is {transactions}.")
            print(f"Your final balance is {lBalance}.")


    else:
        print("Please enter a valid information")