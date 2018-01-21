lista_datos = ["hola", 56, 8, "mundo", 10]
lista_str = []
lista_int = []

for dato in lista_datos:
    if type(dato) == str:
        lista_str.append(dato)
    elif type(dato) == int:
        lista_int.append(dato)

print(lista_int)
print(lista_str)