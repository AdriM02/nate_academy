transformacion = None
resultado = None
simbolo = None
numero_usuario = None

while transformacion != str("FARENHEIT") and transformacion != str("CELSIUS"):
    transformacion = str(input("Para: Celsius a Farenheit (Celsius)    Farenheit a Celsius (Farenheit) -> ")).upper()

numero_usuario = float(input("Número({}) a transformar: ".format(transformacion)))

if transformacion == ("FARENHEIT"):
    resultado = (numero_usuario - 32) / 1.8
elif transformacion == ("CELSIUS"):
    resultado = numero_usuario * 1.8 + 32

if transformacion == ("FARENHEIT"):
    simbolo = "C"
elif transformacion == ("CELSIUS"):
    simbolo = "F"
resultado = round(resultado,1)
print("Tu resultado es {}º{}".format(resultado, simbolo))