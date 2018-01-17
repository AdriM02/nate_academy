tipo_operacion = None
primer_numero = None
segundo_numero = None

while tipo_operacion or primer_numero or segundo_numero == None:
    tipo_operacion = input ("¿Qué operación quieres realizar (multiplicar / sumar / restar)?: ")
    primer_numero = int(input ("Primer número: "))
    segundo_numero = int(input ("Segundo número: "))
resultado = str("Error")


if tipo_operacion == "multiplicar":
    resultado = int(primer_numero * segundo_numero)
elif tipo_operacion == "sumar":
    resultado = int(primer_numero + segundo_numero)
elif tipo_operacion == "restar":
    resultado = int(primer_numero - segundo_numero)
# Me aburría:
elif tipo_operacion == "multiplicar" and segundo_numero == 5:
    print ("Por el culo te la ...")

print ("Resultado: {}".format(resultado))