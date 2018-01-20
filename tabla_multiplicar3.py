numero_tabla = int(input("De que número quieres la tabla de multiplicar: "))
rango_numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiplo in rango_numeros:
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))