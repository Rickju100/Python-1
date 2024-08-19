
texto  = "hello"
vocales = ["a","e","i","o",'u']
vocales_en_texto = []

for letra in texto:
    if letra in vocales:
        vocales_en_texto.append(letra)

print(vocales_en_texto)