#Invertir una lista
def invertir(lista_datos):
    lista_invertida = lista_datos[::-1]
    return lista_invertida
lista = input("Ingrese una lista: ")

lista_ingresada = lista.split()
nueva_lista = invertir(lista_ingresada)

print("Lista invertida: ", nueva_lista )

print("Lista invertida: ", nueva_lista )