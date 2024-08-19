""""Create a list of patient records that stores the names of a doctor's patients: 
Sample list: patient_list = ['name1', 'name2', 'name3', 'name4']
Show this list to the user.
ask the user if they want to add or remove a patient.
Have the user enter the patient's name.
Modify the list based on the users response.
The same name shouldn't be added twice to the list."""


patients = ["Gladys Edwards", #imo is better to make the list this way, more readable
"Renee Garner",
"Saba Meadows",
"Jaydon Dorsey",
"Dewey Poole",
"Martina Marquez",
"Saif Rivera",
"Imran Roberts",
"Rosie Orozco",
"Lester Moore"]
print()
print("The patients list is:")
print(patients)
print()
print("-----Menu-----")
print("If you want to add a patient select 'add'") #Making the options individualy is better at printing to user
print("If you want to delete a patient select 'delete'")
question = input("What option would you like to select: ").capitalize()
#In this code there are several blank prints to separate options, menus, info, etc.. to make the code better for final user

if question == "Add":
    patient = input("Enter the patient's name: ").title() #I preffer to use title instead of capitalize here, because sometimes patiens have 2 names or user input name and last name, and i want both to be capitalize
    if patient not in patients: #With this if, i will make the code avoid to duplicate a patient's name in the list
        patients.append(patient)
    else: 
        print()
        print(f"{patient} is already in the list")
elif question == "Delete":
    patient = input("Enter the patient's name: ").title()
    print()
    print(f"{patient} was removed from the list")
    patients.remove(patient)
else:
    print("Error")

print() #this blank print allows the prompet message to been more profesional
print("The final list is:")
print(patients)