#Eliminar valores duplicados
def borrar_duplicados(lista_datos):
    lista_sinduplicados = list(set(lista_datos))
    return lista_sinduplicados

lista = input("Ingrese una lista: ")
lista_ingresada = lista.split()
sin_duplicados = borrar_duplicados(lista_ingresada)

print("Lista sin duplicados: ", sin_duplicados )