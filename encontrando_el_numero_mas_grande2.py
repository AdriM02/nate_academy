numeros_usuario = []
numero_introducido = ""
largo_lista = 0

while numero_introducido != int and numero_introducido != "FIN":
    numero_introducido = (input("Dime un número para añadirlo / Escribe 'fin' para contarlos: ")).upper()

    while numero_introducido.isdigit():
        numeros_usuario.append(int(numero_introducido))
        largo_lista += 1
        numero_introducido = ""
        print("¡Número añadido!")

if numero_introducido == "FIN":
    if largo_lista > 1:
        print("Has introducido {} números".format(largo_lista))
        print(numeros_usuario)
        exit()
    elif largo_lista == 1:
        print("Has introducido {} número".format(largo_lista))
        print(numeros_usuario)
        exit()
    elif largo_lista == 0:
        print("No has introducido ningún número")
        exit()