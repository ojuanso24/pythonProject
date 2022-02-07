import random
def generar_matrices(a, b):
    # matriz=[[random.randint(0, 99) for x in range(a) for y in range(b)]]
    matriz = []
    for fila in range(a):
        matriz.append([])
        for columna in range(b):
            matriz[fila].append(random.randint(0, 5))
    return matriz
def comparar(matriz1, matriz2):
    iguales=[]
    for x in range(len(matriz1)):
        for y in range(len(matriz1[x])):
            if matriz1[x][y] == matriz2[x][y]:
                iguales.append((x, y))
    return iguales
def suma_vecinos(matriz, x, y):
    suma = matriz[x][y]
    if x > 0:
        suma += matriz[x-1][y]
    if x < len(matriz)-1:
        suma += matriz[x+1][y]
    if y > 0:
        suma += matriz[x][y-1]
    if y < len(matriz[0])-1:
        suma += matriz[x][y+1]
    return suma