"""Create a program that simulates a Tic Tac Toe game.
The program should output the empty board and update through the game.
Once a player wins, a message should indicate who won and print the final board.
If there's a tie, a message should indicate so.
Only use topics seen in the course so far to create it."""

#Empty board

#in this case, with the investigation i did, i can use the dictionary as an individual variable and call it with fstring inside the function
#I prefer to create functions in order to call them over the main code, also always remember that functions needs to be created in the beggining of the code, or they will have some reading issues
def empty_board(spot):
    board = (f"|{spot[1]}|{spot[2]}|{spot[3]}|\n"  #the \n will make the f string to split the values into new lines
            f"|{spot[4]}|{spot[5]}|{spot[6]}|\n"
             f"|{spot[7]}|{spot[8]}|{spot[9]}|")
    print(board)

def check_turn(turn):
    if turn %2 == 0: #this condition will only be true if the  % is valid
        return "O"
    else:
        return "X"

def win_or_tie(spot): #This is the easiest way to set the rules for win or lose, there should be a better and optimal way to improve it, to not make that many conditions, looks really messy (needs to work in this after and make the code better for reading)
    if   (spot[1] == spot[2] == spot[3]) \
        or (spot[4] == spot[5] == spot[6]) \
        or (spot[7] == spot[8] == spot[9]):
        return True

    elif   (spot[1] == spot[4] == spot[7]) \
        or (spot[2] == spot[5] == spot[8]) \
        or (spot[3] == spot[6] == spot[9]):
        return True

    elif (spot[1] == spot[5] == spot[9]) \
        or (spot[3] == spot[5] == spot[7]):
        return True
    
    else: return False

#this is a dictionary that will help me to map values in order to compare if the player's choosen spot is available


spot = {1:"1", 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:"9"} 
"""this dictioriary values' will be set up this way   
|1|2|3|
|4|5|6|
|7|8|9|

"""
def tic_tac_toe(spot):
    turn = 0

    while True:
        empty_board(spot)
        chose = input("Chose a number: ")

        if chose.capitalize == "End":
            break
        elif str.isdigit(chose) and int(chose) in spot: #this conditional, will look if the number or letter is in the list
            if not spot[int(chose)] in {"X","O"}: #This will keep not available the option to chose the same spot
                turn += 1
                spot[int(chose)] = check_turn(turn)

            if win_or_tie(spot):
                empty_board(spot)
                print("Win")
                break
            elif turn == 9:
                empty_board(spot)
                print("Tie")
                break
        else:
            print("Please Choose an empty spot")
            
tic_tac_toe(spot) #since i create all the code as functions here i only need to call the function, also i can create this document as a module after and can call the functions for better projects or portafolio (Which i will)

