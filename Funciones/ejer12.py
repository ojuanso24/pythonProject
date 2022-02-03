import random


def genenara_matriz_tamanoRandon():
    columnas = range(random.randint(2, 6))
    filas = range(random.randint(2, 6))
    return [[random.randint(0, 100) for x in columnas] for y in filas]


print(genenara_matriz_tamanoRandon())