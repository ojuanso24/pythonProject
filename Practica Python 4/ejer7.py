tamano = 5
matriz = [[0 for x in range(tamano)] for y in range(tamano)]
totalFilas = [0 for x in range(tamano)]
totalColumnas = [0 for x in range(tamano)]
try:
    for i in range(len(matriz)):
        entrada = input("Introduce fila " + str(i + 1) + ": ").split(" ")
        if len(entrada) == tamano:
            matriz[i] = entrada
        else:
            print("la columna mal introducida sera igual a: 0 0 0 0 0")
except:
    print("Datos erroneos")
for x in range(len(matriz)):
    for y in range(len(matriz)):
        totalColumnas[x] += int(matriz[y][x])
        totalFilas[x] += int(matriz[x][y])
print("Total Filas", totalFilas)
print("Total Columnas", totalColumnas)