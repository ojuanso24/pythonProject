import random


def genenaraMatriz(fila, columna, maxAleatorio = 100, minAleatorio = 0):
    return [[random.randint(minAleatorio, maxAleatorio) for a in range(fila)] for b in range(columna)]


def genenaraMatrizTamanoRandon():
    return [[random.randint(0, 100) for x in range(random.randint(1, 100))] for y in range(random.randint(1, 10))]


def genenaraMatrizTamanoRandon2():
    return [[random.randint(0, 100) for x in range(random.randint(2, 6))] for y in range(random.randint(2, 6))]


def iguales(lista1, lista2):
    listaAux = []
    for x in range(len(lista1)):
        for y in range(len(lista1[x])):
            if lista1[x][y] == lista2[x][y]:
                listaAux.append((x, y))
    return listaAux


def compararMatricesGuion(lista1, lista2):
    listaAux = [["-" for x in range(len(lista1[0]))] for y in range(len(lista1))]
    for x in range(len(lista1)):
        for y in range(len(lista1[x])):
            if lista1[x][y] == lista2[x][y]:
                listaAux[x][y] = lista1[x][y]
    return listaAux

def sumaVecimos(x, y, matriz):
    suma = matriz[x][y]
    if x > 0:
        suma += matriz[x-1][y]
    if x < len(suma) - 1:
        suma += matriz[x + 1][y]
    if y > 0:
        suma += matriz[x][y - 1]
    if y < len(matriz[0]) -1:
        suma += matriz[x][y + 1]
    return suma

print(genenaraMatrizTamanoRandon2())