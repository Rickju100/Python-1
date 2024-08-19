from getpass import getpass


player1= getpass("Player 1 enter the word to guess: ").capitalize()
count = 0
total = 6
while count <= 6:
    if  count < 6:
        print (f"you have {total} attempts") 
        player2 = input("Player 2 enter the guess: ").capitalize()
        if player1 == player2:
            print("Congratulations you have guess the word!")
            print(f"The word was {player1}.")
            break
        else:
            print("Try it again")
            count += 1
            total -= 1
    else:
        print("You have no attempts!")
        print(f"The word was {player1}.")
        print("Best luck next time!")
        break
