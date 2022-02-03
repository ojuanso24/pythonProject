import random


def genenara_matriz_tamanoRandon():
    columnas = range(random.randint(2, 6))
    filas = range(random.randint(2, 6))
    return [[random.randint(0, 100) for x in columnas] for y in filas]


def cuadrado(matriz):
    if len(matriz) == len(matriz[0]):
        total = 0
        for i in range(len(matriz)):
            print(i, matriz[i][i])
            total += matriz[i][i]
        return total
    return None


print(cuadrado(genenara_matriz_tamanoRandon()))