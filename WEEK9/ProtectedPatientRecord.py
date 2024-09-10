"""Take the practice Patient Record Script and add authentication (user should be prompted for username and password BEFORE being able to see the case list).
The "database" with the usernames/passwords MUST be inside a dictionary.
The user is able to add or remove users from the dictionary.
After authenticating, the user is able to add or remove cases."""

auth = {
    "Carlos":"1234",
    "Pedro":"2345",
    "Juan":"1234",
    "Raul":"2345",
    "Rodrigo":"1234",
    "Paul":"2345",
    "Christian":"1234",
    "Pascal":"2345",
}

print("Please enter your authentication info")
username = input("Enter your Username: ").capitalize()
password = input("Enter your Password: ")

"""if username in auth.keys() and password in auth.values():
    print(f"Welcome {username}!")
    print("Authentification Success!")"""
#here i tried tuples to use the items built in function for dictionaries, and match key and value at the same time
data = (username,password)
if data in auth.items():
    print(f"Welcome {username}!")
    print("Authentification Success!")

for i in auth.keys():
    