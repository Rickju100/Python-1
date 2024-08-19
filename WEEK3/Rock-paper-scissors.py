"""Create a two player script that plays "rock-paper-scissors". 
(Optional) Research how to hide the input from the users.
Rules:
Paper beats rock.
Rock beats scissors.
Scissors beats paper.
A player wins with 3 of 5 games."""

from getpass import getpass

COUNT = 0
Player1_wins = 0
Player2_wins = 0



print("Hello User")
player_1 = input("Select name for player 1: ").capitalize()
player_2 = input("Select name for player 2: ").capitalize()
print()
print("Here is the menu")
print("Rock, Paper, Scissors")
print()

while COUNT <= 5:
    if Player1_wins == 3 or Player2_wins == 3:
        break
    else:
        player_a = getpass("Player 1. Select the option you prefer: ").capitalize()
        player_b = getpass("Player 2. Select the option you prefer: ").capitalize()
        if player_a == "Rock":
            if player_b == "Rock":
                print(f"{player_1} and {player_2} you have scored a Tie")
                print(f"You both have choosen {player_a}")
                Player1_wins += 1
                Player2_wins += 1
            elif player_b == "Paper":
                print(f"{player_2} win")
                print(f"{player_1} you have choosen {player_a}")
                print(f"{player_2} you have choosen {player_b}")
                Player2_wins +=1
            elif player_b == "Scissors":
                print(f"{player_1} Win")
                print(f"{player_1} you have choosen {player_a}")
                print(f"{player_2} you have choosen {player_b}")
                Player1_wins +=1
            COUNT += 1
        elif player_a == "Paper":
            if player_b == "Paper":
                print(f"{player_1} and {player_2} you have scored a Tie")
                print(f"You both have choosen {player_a}")
                Player1_wins += 1
                Player2_wins += 1
            elif player_b == "Rock":
                print(f"{player_1} Win")
                print(f"{player_1} you have choosen {player_a}")
                print(f"{player_2} you have choosen {player_b}")
                Player1_wins +=1
            elif player_b == "Scissors":
                print(f"{player_2} win")
                print(f"{player_1} you have choosen {player_a}")
                print(f"{player_2} you have choosen {player_b}")
                Player2_wins +=1
            COUNT += 1
        elif player_a == "Scissors":
            if player_b == "Scissors":
                print(f"{player_1} and {player_2} you have scored a Tie")
                print(f"You both have choosen {player_a}")
                Player1_wins += 1
                Player2_wins += 1
            elif player_b == "Rock":
                print(f"{player_2} win")
                print(f"{player_1} you have choosen {player_a}")
                print(f"{player_2} you have choosen {player_b}")
                Player2_wins +=1
            elif player_b == "Paper":
                print(f"{player_1} Win")
                print(f"{player_1} you have choosen {player_a}")
                print(f"{player_2} you have choosen {player_b}") 
                Player1_wins +=1
            COUNT += 1
        
        else:
            break

print()
if Player1_wins > Player2_wins:
    print(f"Congratulations {player_1} you are the winner!")
    print(f"You had {Player1_wins} wins!")
    print(f"Total score= {player_1}: {Player1_wins} and {player_2}: {Player2_wins}")
else:
    print(f"Congratulations {player_2} you are the winner!")
    print(f"You had {Player2_wins} wins!")
    print(f"The total score was {player_1}: {Player1_wins} and {player_2}: {Player2_wins}")