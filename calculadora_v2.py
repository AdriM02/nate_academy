tipo_operacion = None
primer_numero = None
segundo_numero = None

while tipo_operacion == None or primer_numero == None or segundo_numero == None:
    tipo_operacion = (input("¿Qué operación quieres realizar (multiplicar / sumar / restar)?: ")).upper()
    while tipo_operacion != ("MULTIPLICAR") and tipo_operacion != ("SUMAR") and tipo_operacion != ("RESTAR"):
        print('Solo puedes escribir "multiplicar", "sumar" o "restar"')
        tipo_operacion = (input("¿Qué operación quieres realizar (multiplicar / sumar / restar)?: ")).upper()

    primer_numero = int(input ("Primer número: "))
    segundo_numero = int(input ("Segundo número: "))
resultado = str("Error")

################## Me aburría ##################
if tipo_operacion == "MULTIPLICAR" and segundo_numero == 5:
    resultado = int(primer_numero * segundo_numero)
    print ("Por el culo te la ...")
    print("Resultado: {}".format(resultado))
    exit()
################################################

elif tipo_operacion == "SUMAR":
    resultado = int(primer_numero + segundo_numero)
elif tipo_operacion == "RESTAR":
    resultado = int(primer_numero - segundo_numero)
elif tipo_operacion == "MULTIPLICAR":
    resultado = int(primer_numero * segundo_numero)

print ("Resultado: {}".format(resultado))