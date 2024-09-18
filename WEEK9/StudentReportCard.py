"""Create a script that generates a report card for all students available.
The program must follow the specifications below:
The grades and subjects for each student must be stored in a nested dictionary.
Create a dictionary called student_data. It will store the grades and subjects for each student. The keys are the name of each student and the values are dictionaries containing subject: grade pairs.
Ask the user how many students they want to generate.
For each student, ask for their name and the number of subjects they'll have in the report card.
For each subject ask for the subject's name and the score obtained.
Finally, using f-strings output the report card for each student showing their name, subject: grade."""

student_data = {}

studentsNum = int(input("How many Students would you like to generate?: "))

for i in range(studentsNum):
    sName = input(f"Enter the student name {i+1}: ").capitalize()

    subjects = {}

    SubjNum = int(input("How many subjects will they have in the report card?: "))

    for j in range(SubjNum):
        subName = input(f"Enter the subject name {j+1} : ").capitalize()
        subGrade = float(input("Enter the Grade: "))

        subjects[subName] = subGrade
        #i can also write this as subjects.update({subName:SubGrade})

    student_data[sName] = subjects #Remember this is part of the main for loop
    #i can also write this as subjects.update({sName,subjects})

print()
print("Students Grade's Card")
print()

for sName,subjects in student_data.items(): #Remember to use .items(), .value() or .Key() otherwise the code will print an error, too many values, 2 expected 
    print(f"{sName}")
    for subName, subGrade in subjects.items():
        print(f"{subName}: {subGrade}")
    print()
print()
