numero_solucion = int(input("Número a adivinar (Que tu amigo no lo vea): "))
numero_prueba = None

while numero_prueba != numero_solucion:
    numero_prueba = int(input("Adivina el número: "))

if numero_prueba == numero_solucion:
    print("¡Has acertado! Era {}".format(numero_solucion))
else:
    print("Solo puedes escribir números")