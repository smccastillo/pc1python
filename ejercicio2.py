# Calcular el monto de la propina
monto = float(input("Por favor ingresar el monto total de consumo: "))
propina = float(input("¿Cuál es el porcentaje de propina que desea dejar?: "))

montopropina = (monto * propina)/100

print(f"Monto total de propina a dejar: {montopropina:.2f}")
