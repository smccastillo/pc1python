# Calcular el peso total del paquete

Wpayaso = 112
Wmuñeca = 75
print("Vamos a calcular el peso total del paquete")
Qpayasos = int(input("Ingresar el número de payasos del paquete: "))
Qmuñecas = int(input("Ingresar el número de muñecas del paquete: "))

Wtotal = (Wpayaso*Qpayasos)+(Wmuñeca*Qmuñecas)
print(f"El peso total en gramos del paquete es: {Wtotal}")