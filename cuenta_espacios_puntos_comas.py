texto_usuario = input("Introduce una frase: ")

n_espacios = 0
n_puntos = 0
n_comas = 0

espacio = [" "]
punto = ["."]
coma = [","]

for caracter in texto_usuario:
    if caracter in espacio:
        n_espacios += 1
    elif caracter in punto:
        n_puntos += 1
    elif caracter in coma:
        n_comas += 1

print("espacios = {}".format(n_espacios))
print("puntos = {}".format(n_puntos))
print("espacios = {}".format(n_comas))