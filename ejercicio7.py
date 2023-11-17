# OPERACIONES SEGUN ELECCIÓN

n1 = int(input("Ingresar el primer número: "))
n2 = int(input("Ingresar el segundo número: "))
print(f"Los números ingresados son {n1} y {n2}")

print("Elija una opción de operación: ")
print("1 Suma de ambos números")
print("2 Resta de ambos números (primero-segundo)")
print("3 Multiplicación de ambos numeros")

seleccion =input("Ingrese el numero de la opción deseada: ")
if seleccion == "1":
    resultado = n1 + n2
    print(f"La suma de los dos números es: {resultado}")
elif seleccion == "2":
    resultado = n1 - n2
    print(f"La resta (primer número - segundo número) es: {resultado}")
elif seleccion == "3":
    resultado = n1 * n2
    print(f"La multiplicación de los dos números es: {resultado}")
else:
    print("Opción no válida. Por favor, ingrese 1, 2, o 3.")