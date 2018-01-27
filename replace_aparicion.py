texto = input("Introduce una frase: ")

numero_posicion = 1
posicion = 0
nuevo_texto = ""

while len(texto) > posicion:
    if texto[posicion] == "a" or texto[posicion] == "e" or texto[posicion] == "i" or texto[posicion] == "o" or texto[posicion] == "u":
        nuevo_texto += str(numero_posicion)
        numero_posicion += 1
        posicion += 1
    else:
        nuevo_texto += texto[posicion]
        posicion += 1
print(nuevo_texto)