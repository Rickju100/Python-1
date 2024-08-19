

active = True

while active:
    x = input("Tengo dinero? ").capitalize() #recordar siempre capitalize con (), porque es una funcion, sino no funciona

    if x == "Si":
        print("Ire al cine")
        y = input("Tengo Hambre?: ").capitalize() #recordar siempre capitalize con (), porque es una funcion, sino no funciona
        if y == "Si":
            print("Compro Palomitas")
            active = False
        else:
            print("Me compro un Helado")
            active = False

    else:
        print("Ire a la Sabana")
        z = input("Estoy cansado? ").capitalize()  #recordar siempre capitalize con (), porque es una funcion, sino no funciona
        if z == "Si":
            print("Me acuesto")
            active = False
        else:
            print("Mejengueo")
            active = False
