"""Create a program that stores 3 grades for 5 students in the following way:
All information will be stored in a list.
Each element of the list will be a tuple that contains two elements: the student's name and a list with the 3 grades.
The names and the grade must be received as an input.
After all the information is gathered, use a f string to print the student's name and the average of the student's grades."""

studentsResult = []


for i in range(2):
    name = input(f"Name {i+1}: ")
    #I tried to create a list to append name, but in the print, it will have the structure [name,name][grade grade grade], instead of name,grade, name, grade

    grades = []
    for grade in range(3):
        Grade = int(input(f"Enter the Grade {grade+1} : "))#Here i learned that if i place the grade+1, it will print it as a sum in every iteration in the loop
        grades.append(Grade) #Carefull to not append grade, already did that mistake, it will not store the Grades, it will store the values that grade takes in the loop, 0,1,2

   #THIS IS THE TUPPLE, REMEBER TUPPLE USE () AS STRUCTURE, INSTED OF [] FOR LIST
    student = (name,grades) #Here in the tupple, i place both variables created in the loop
    studentsResult.append(student) #If i dont place the tupple in the list, i can not append. Tupples can only index and count



#here i need to create another loop, to print the student's name and the average of the student's grades
#In this loop, i make result to take the value of each item in studentsResult, after i will take only the index 1, which means grade
for result in studentsResult:
    cadaEstudiante = result[0]
    notas = result[1]
    averageGrades = sum(notas) / len(notas)
    print(f"The student {cadaEstudiante} has an average grade of {averageGrades}".rstrip("0").rstrip(".")) #In this order, rstrip will first remove the extra zero, and after will remove the dot