numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("¡Número añadido!")

numero_pequeno = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El número más paqueño de {} es {}".format(numeros_usuario, numero_pequeno))