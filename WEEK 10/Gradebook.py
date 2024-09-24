"""Create 3 dictionaries that contain the following keys-values:
"name": Student's name
"homework": A list with the grade of 4 homeworks.
"quizzes": A list with the grade of 3 quizzes.
"tests": A list with the grade of 2 tests.
*You can choose if you want to fill this information from a user input or manually. If done through a user input, create a function called fill_grades(dictionary) that receives 1 student dictionary as parameter and asks the user for all the information specified above (the grades can be filled with a for and using the random.randint function to fill them with random values between 0 and 100).
Create a list that contains the names of the students.
Write a function average(list) that receives a list of numbers and returns the average of that list.
Write a function called get_average(dictionary) that receives a dictionary as parameter and returns the weighted average of their grades (the weights are how much percentage each item takes of the final grade).
Inside the function create variables that store the result of average(list) of the different grades in a student dictionary.
Multiply the 3 averages of each student by their weights and return the sum of the resulting scores.
Weights: Homework is 10%, quizzes are 30% and tests are 60%.
Write a function called get_letter_grade(int) that receives a student grade as parameter.
Depending on the student's grade, the function should print out the following message:
Score is 90 or above: return "A"
Score is 80 or above: return "B"
Score is 70 or above: return "C"
Score is 60 or above: return "D"
Score below 60: return "F"
Write a function called get_class_average(list) that receives a list that contains the students' names.
Inside the function create a new empty list called scores.
For each student in the parameter list, call the get_average() function and add the result to the scores list.
Return the result of average(list) with scores list.
In the main code:
Print all the students information formatted as:
Name: Student's name
Homeworks: Homeworks scores.
Quizzes: Quizzes scores.
Tests: Tests scores.
Letter grade: get_letter_grade() result.
Then print the class average result calling the get_class_average(list) function."""

sNames = {}
homework = {}
quizzes = {}
tests = {}


num = int(input("How any students would you like to add?: "))

for i in range(num):
    Students = input("Enter the students name: ")

    Homework = {}
    for j in range(1,5):
        homework = float(input("enter the grade {j+1}: "))

    Homework["Grades"] = homework

sNames[] = stu

print(sNames)


