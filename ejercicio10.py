# ELIMINAR CARACTERES POR POSICION
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
posicion = [0, 4, 5]
lista_resultado = [valor for i, valor in enumerate(lista_muestra) if i not in posicion]
print("Resultado esperado:", lista_resultado)
