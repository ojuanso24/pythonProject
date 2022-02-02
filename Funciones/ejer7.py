def cadenas_mas_largas(lista):
    listaPalabras = []
    lista = sorted(lista, key=len, reverse=True)
    contador = 0
    while len(lista[contador]) == len(lista[0]):
        listaPalabras.append(lista[contador])
        contador += 1
    return listaPalabras


listaNombre = ["juan", "ana", "jose", "pepe", "pablo"]
print(cadenas_mas_largas(listaNombre))
