#Autos brand

Japones = ["Honda", "Mitsubishi", "Toyota"]

brand = input ("Enter a Car brand: ").capitalize()

if brand in Japones:
    print (f"{brand} is a Jappanesse Car brand")
else:
    print(f"{brand} is not a Jappannesse Car Brand")

#also remember i can print positions in the list
print(Japones[1])    

#I can update a list value with [] and the index example
Japones[0] = "Nintendo"
print(f"The modified value is {Japones[0]}") 

#I can review how long is the list
print(len(Japones))

#Can use del to remove a value from the list, but needs to specify the index, or i will delet all the list
del Japones[0]
print(Japones)

#i can use sort to order data, also reverse 