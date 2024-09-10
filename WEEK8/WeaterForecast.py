import random
import datetime as dt
"""Using f strings create a script that prints the following disclosure:
-------------------------------------
Hello (person's name), 
Today is (day of the week)
The weather for today is ( weather forecast ) 
-------------------------------------
Person's name must be requested from the user.
Day of the week must be accurate.
The weather forecast must be chosen randomly from these options: Sunny, Cloudy, Windy, Foggy, Rainy.
The values of the weather cannot be modified so they must be stored in a tuple."""

name = input("Enter your name: ").capitalize()
weatertuple = ("Sunny", "Cloudy", "Windy", "Foggy", "Rainy")
#To ramdom a value from the tuple
tRandom = random.choice(weatertuple)
today = dt.date.today().strftime("%A")


print()
print(f"Hello {name} \nToday is {today} \nThe weather for today is {tRandom}")
print()