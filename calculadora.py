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

print ("Resultado: {}".format(resultado))