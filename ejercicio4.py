# Suma de número enteros

num = int(input("Ingrese un número entero positivo: "))
if num <= 0:
    print("El número ingresado no es un entero positivo.")
else:
    suma = num * (num + 1) // 2
    print(f"La suma de los {num} primeros enteros positivos es: {suma}")