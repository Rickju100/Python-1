"""Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter. The script takes a string word as input and prints the equivalent scrabble score for that word.
The scores for each letter MUST be stored in a dictionary as shown below.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}"""

score = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2,
    "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, 
    "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, 
    "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, 
    "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, 
    "z": 10
    }
print()
print("Welcome to Scrabble game")
print()

def scrabble():
    while True: 

        ToL = input("Write 'Try' for try a letter or 'Leave' to end the game: ").lower()


        if ToL == "try":
            word = input("Enter a letter: ").lower()
            if word in score.keys():
                print(score.get(word))
        elif ToL == "leave":
            print("Thanks for playing")
            break 
        else:
            print(f"{ToL} is not a valid Option!")
            print("Enter a valid Option")

scrabble()