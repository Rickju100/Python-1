"""Write a Python code that checks if a word is an isogram.
**An isogram is word that has no repeating letters, consecutive or non-consecutive.
The code must print "is isogram" if the word is an isogram or "Not an isogram" if it's not.
Upper and lower case letters should be considered the same. Use the .lower() method for all letters to be converted to lower case.
Sample data:
"Demographics" -> is isogram
"Hello" -> Not an isogram
"Identity" -> Not an isogram"""

word = input("Enter a word: ").lower()
word_list = []

for i in word:
    if i in word_list:
        print(f"{word} is not an isogram")
        break
    word_list.append(i) #This condition is placed here, because will never be executed only if the if is not possible
else: #Visual itself point this else below the for. THis else is started when the loop end normally https://www.youtube.com/watch?v=WUF3ZQoyb8Y
    print(f"{word} is an isogram")
        

 
