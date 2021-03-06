# Antonio Carrión Ramírez
# Practica de examen
import random


def GenerarCiudad(filas, columnas):
    ciudad = []
    for fila in range(filas):
        ciudad.append([])
        for columna in range(columnas):
            ciudad[fila].append("SANO")
    ciudad[random.randint(0, filas - 1)][random.randint(0, columnas - 1)] = "I-0 "  # Añado un espacio en para que la matriz quede bien tabulada
    return ciudad


def MuestraCiudad(ciudad, dia):
    stringCiudad = "Día: " + str(dia) + "\n \t"
    for i in range(len(ciudad)):
        for j in range(len(ciudad[i])):
            if j == len(ciudad[i]) - 1:
                stringCiudad += ciudad[i][j] + '\n \t'
            else:
                stringCiudad += ciudad[i][j] + '  '
    return stringCiudad


def Contagiar(ciudad):
    dia = 0
    contagios = 1
    personas = len(ciudad) * len(ciudad[0])
    print(MuestraCiudad(ciudad, dia))
    while personas > contagios:
        infectado = "I-" + str(dia) + " "
        for y in range(len(ciudad)):
            for x in range(len(ciudad[y])):
                if ciudad[y][x] == infectado:
                    if y > 0 and ciudad[y - 1][x] == "SANO":
                        ciudad[y - 1][x] = "I-" + str(dia + 1) + " "
                        contagios += 1
                    if y < len(ciudad) - 1 and ciudad[y + 1][x] == "SANO":
                        ciudad[y + 1][x] = "I-" + str(dia + 1) + " "
                        contagios += 1
                    if x > 0 and ciudad[y][x - 1] == "SANO":
                        ciudad[y][x - 1] = "I-" + str(dia + 1) + " "
                        contagios += 1
                    if x < len(ciudad[0]) - 1 and ciudad[y][x + 1] == "SANO":
                        ciudad[y][x + 1] = "I-" + str(dia + 1) + " "
                        contagios += 1
        dia += 1
        print(MuestraCiudad(ciudad, dia))
    return dia


ciudad = GenerarCiudad(int(input("Inserte las filas: ")), int(input("Inserte las columnas: ")))
print("Días totales: " + str(Contagiar(ciudad)))