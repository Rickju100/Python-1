"""
Crear un juego que muestre un menu al inicio con 3 opciones:
1 Easy (3 paises)
2 Medium (5 paises)
3 Hard (10 paises)
Utilizar append para almacenar cada valor ingresado por el usuario
"""

countrylist = []
count = 0

print("Here is the menu 1.Easy 2.Medium 3.Hard")
level = int(input('Choose an option: '))


if level == 1:
    countrys_count = 3 
        
elif level == 2:
    countrys_count = 5

elif level == 3:
    countrys_count = 10 
else:
    print("Enter a valid option")
    

while count< countrys_count:
    Country = input("Enter a country name: ").capitalize()
    count += 1

print(countrylist)