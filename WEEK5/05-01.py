#We use for loop when the conditions does not matters, only the turn matters
list = [1,2,3,4,5,6]
result = 0


for i in list:
    print(i)
    result += i #THis is for sum every value that i takes over the iteration of the list

print(result)

#I can loop for every letter in a word

for i in "text":
    print("Hello")