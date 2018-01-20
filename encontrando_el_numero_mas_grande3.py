numeros_usuario = []
numero_introducido = ""
suma_numeros = 0

while numero_introducido != int and numero_introducido != "FIN":
    numero_introducido = (input("Dime un número para añadirlo / Escribe 'fin' para contarlos: ")).upper()

    while numero_introducido.isdigit():
        numeros_usuario.append(float(numero_introducido))
        numero_introducido = ""
        print("¡Número añadido!")

if numero_introducido == "FIN":
    for numero in numeros_usuario:
        suma_numeros += numero
    print(suma_numeros / len(numeros_usuario))