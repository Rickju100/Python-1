# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check for a tie
def check_tie(board):
    return all([cell != " " for row in board for cell in row])

# Function to play the game
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    # Game loop
    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        # Check if the move is valid
        if board[row][col] == " ":
            board[row][col] = current_player

            # Check if the current player has won
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            # Check for a tie
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                # Switch players
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move, try again.")

# Start the game
play_game()
