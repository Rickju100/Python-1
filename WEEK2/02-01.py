"""
Si tengo dinero, ire al cine, 
si no tengo dinero, ire a la sabana 
si voy al cine y tengo hambre, compro palomitas
si no tengo hambre me compro un helado
Si fui a la sabana y estoy cansado, me acuesto
si fui a la sabana y no estoy cansado mejengueo
"""

x = input("Tengo dinero? ").capitalize() #recordar siempre capitalize con (), porque es una funcion, sino no funciona

if x == "Si":
    print("Ire al cine")
    y = input("Tengo Hambre?: ").capitalize() #recordar siempre capitalize con (), porque es una funcion, sino no funciona
    if y == "Si":
        print("Compro Palomitas")
    else:
        print("Me compro un Helado")

else:
    print("Ire a la Sabana")
    z = input("Estoy cansado? ").capitalize()  #recordar siempre capitalize con (), porque es una funcion, sino no funciona
    if z == "Si":
        print("Me acuesto")
    else:
        print("Mejengueo")
