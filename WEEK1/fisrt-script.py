#input first and last name and age, output users full name and year he was born

first_name = input("what is your first name?: ").capitalize()
last_name = input('what is your last name?: ').capitalize()
Age = int(input('What is your age? ')) 
DOB = 2024 - Age

print(f'Your name is {first_name} {last_name} and you were born in {DOB}')
print(first_name)