from matrices1 import generar_matrices, comparar, suma_vecinos
matriz1 = generar_matrices(3, 5)
matriz2 = generar_matrices(3, 5)
print(matriz1)
print(matriz2)
iguales = comparar(matriz1, matriz2)
for x in range(len(matriz1)):
    for y in range(len(matriz1[x])):
        if matriz1[x][y] == matriz2[x][y]:
            print(str(matriz1[x][y]), end="\t")
        else:
            print("-", end="\t")
    print()
print(suma_vecinos(matriz1, 1, 1))