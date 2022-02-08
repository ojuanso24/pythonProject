import random


def GenerarMatriz(numero, nombre):
    matriz = []
    contador = 0
    for fila in range(numero):
        matriz.append([])
        for columna in range(numero):
            introducir = random.randint(0, len(matriz))
            if introducir == 0:
                matriz[fila].append(nombre[contador])
                contador += 1
                if contador >= len(nombre):
                    contador = 0
            else:
                matriz[fila].append(introducir)
    return matriz


def MostrarMatriz(matriz):
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            print(matriz[y][x], end="\t")
        print()


def Fastidiar(matriz, nombre):
    tamanoMaximo = len(matriz) -1
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "y", "x", "z"]

    letra = letras[random.randint(0, len(letras) - 1)]
    while nombre.find(letra) == -1:
        matriz[random.randint(0, tamanoMaximo)][random.randint(0, tamanoMaximo)] = letra
        letra = letras[random.randint(0, len(letras) - 1)]


def ComprobarResultado(matriz, nombre):
    nombreDiccionario = {}
    for i in nombre:
        if i in nombreDiccionario:
            nombreDiccionario[i] += 1
        else:
            nombreDiccionario[i] = 1

    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if matriz[y][x] in nombreDiccionario:
                nombreDiccionario[matriz[y][x]] -= 1

    for j in nombreDiccionario.values():
        if j > 0:
            return False
    return True
