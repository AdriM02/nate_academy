numero_tabla = int(input("De que número quieres la tabla de multiplicar: "))

for multiplo in range(5, 16):
    if multiplo % 2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))