# CALCULAR PRECIO DE ENTRADA SEGUN LA EDAD

Edad = int(input("Por favor ingrese su edad: "))
if Edad<4:
    entrada = 0
elif 4<= Edad <= 18:
    entrada = 5
else:
    entrada = 10

print(f"El precio de la entrada correspondiente es: {entrada}")