
"""Write a Python program to check whether a letter is a vowel or consonant and print the result.
The letter will be obtained as a user input.
If the user enters something other than a letter output a warning message."""

#There should be a better way to review if the input is a vowel or consonant, but i preffer to make lists
vowels = ["a","e","i","o","u"]
consonants = ["b","c","d","f","g","h","j","k","k","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]


Active = True 

while Active:

    letter = input('Enter a leter to verify: ').lower()

    if letter in vowels or letter in consonants: #really important, to use "letter in" in both values of condition
        if letter in vowels:
            print('The letter is a vowel')
        else:
            print('The letter is a consonant')
        Active =  False #I prefer to make the condition change as globlal here, because both scenarios leave the loop, could've done a menu 
    else:
        print(f'{letter} is not a letter!')
        print('Please enter a valid value.')