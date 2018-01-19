texto_usuario = input("Introduce una frase: ")

n_mayus = 0
mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for caracter in texto_usuario:
    if caracter in mayuscula:
        n_mayus += 1

print("mayusculas = {}".format(n_mayus))
