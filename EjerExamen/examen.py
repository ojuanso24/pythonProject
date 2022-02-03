import random
from copy import deepcopy

def GenerarCiudad(filas = 7, columnas= 7):
    matriz = [["SANO" for x in range(filas)] for y in range(columnas)]
    matriz[random.randint(0, columnas - 1)][random.randint(0, filas - 1)] = "I-0"
    return matriz


def MostrarCiudad(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="   ")
        print()


def Contagiar(matriz):
    infestados = 1
    contador = 1
    print(len(matriz), len(matriz[0]))
    total = (len(matriz) * len(matriz[0]))
    print(total)
    matrizAux = deepcopy(matriz)
    for y in range(len(matriz)):
        for x in range(len(matriz)):
            if matriz[y][x] != "SANO":
                if x > 0:
                    matrizAux[y][x - 1] = "I-" + str(contador)
                    infestados += 1
                if x < len(matriz[x]) - 1:
                    matrizAux[y][x + 1] = "I-" + str(contador)
                    infestados += 1
                if y > 0:
                    matrizAux[y - 1][x] = "I-" + str(contador)
                    infestados += 1
                if y < len(matriz[y]) - 1:
                    matrizAux[y + 1][x] = "I-" + str(contador)
                    infestados += 1
                contador += 1
    matriz = deepcopy(matrizAux)
    MostrarCiudad(matriz)
    print()
    print("")

def infectar(matriz):

    # MostrarCiudad(matrizAux)


# filas1 = int(input("Filas?: "))
# columnas1 = int(input("Columnas?: "))
# print(GenerarCiudad(filas1, columnas1))

ciudad = GenerarCiudad()
MostrarCiudad(ciudad)
print()
Contagiar(ciudad)