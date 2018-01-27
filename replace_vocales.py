string_usuario = input("Escribe una frase: ")
vocales_minusculas = ["a", "e", "i", "o", "u"]
vocales_mayusculas = ["A", "E", "I", "O", "U"]

for vocal_may in vocales_mayusculas:
    string_usuario = string_usuario.replace(vocal_may, "I")

for vocal_min in vocales_minusculas:
    string_usuario = string_usuario.replace(vocal_min, "i")

print(string_usuario)