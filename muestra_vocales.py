texto_usuario = (input("Introduce una frase: ")).upper()

vocales = ["A", "E", "I", "O", "U"]
vocales_en_frase = []

for caracter in texto_usuario:
    if caracter in vocales:
        vocales_en_frase.append(caracter)

print("vocales = {}".format(vocales_en_frase))
