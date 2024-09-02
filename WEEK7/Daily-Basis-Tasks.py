import pythonping as pinger
import datetime as dt

#For this project i prefered to create all the code as functions to practice functions, but also for a future module that i can use in future projects

def pinginfo(): 
    print()
    pingYoN = input("Would you like to calculate the ping? Y/N: ").capitalize()
    print(pingYoN)


    if pingYoN == "Y":
        print("The menu is 1.Site 2.IP 3.Both. 4. Leave")
        menu = input("Enter the option number: ")
        if menu in ["1","2","3"]:
            if menu == "1":
                site = input("Enter the site: ").lower()
                print(pinger.ping(site,count=4))
            elif menu == "2":
                ip = input("Enter the ip: ")
                print(pinger.ping(ip))
            elif menu == 3:
                site = input("Enter the site: ").lower()
                ip = input("Enter the ip: ")
                print(pinger.ping(site,count=4))
                print(pinger.ping(ip))
            elif menu =="4":
                print("You are leaving!")



def today():
    print()
    print(f"Today's date is: {dt.date.today()}")
    print("Here comes the time formats!!")
    print(f"The firt format is: {dt.date.today().strftime("%d/%m/%Y")}")
    print(f"The second format is: {dt.date.today().strftime("%d/%B/%Y")}")
    print()

def timeFuture():
    for i in range(5):
        today = dt.date.today()
        num = i+1
        future = today + dt.timedelta(days=num)

        daisy = future.strftime("%A")
        dayFormat = future.strftime("%d/%B/%Y")
        #Since im learning cammelCase in JS, i try it here in the variable name  
        print(f"{daisy} will be: {dayFormat}")
    print()

def DOB():
    print("Enter your DOB")

    today = dt.datetime.today()
    nacimiento = input("Enter your date of birth (YYYY-MM-DD): ") #This is the only valid format i was able to make the code works Y-Y
    dob = dt.datetime.strptime(nacimiento, "%Y-%m-%d")
    age = today.year - dob.year
    print()
    print(f"Your age is {age}!")
    print()

def mainMenu():
    while True:
        print("Welcome!")
        print("Here is the menu. 1.Get the Ping 2.Get the date 3.Get the next 5 days 4. Give the DOB. 5. Leave")
        mainMenu = input("Select the valid option: ")
        if mainMenu in ["1","2","3","4"]:
            if mainMenu == "1":
                pinginfo()
            elif mainMenu =="2":
                today()
            elif mainMenu =="3":
                timeFuture()
            elif mainMenu == "4":
                DOB()
        else:
            print("Thanks for using the app")
            break
#This will call the menu function where all the functions are set up 
mainMenu()