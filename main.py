# 14.- Escribir un programa que dándole un número (entre 2 y 40) imprima un triángulo como el de la figura.
#   Nivel: 4          Nivel: 3           Nivel: 2
#      XX                 X                 XX
#     XXXX               XXX               XXXX
#    XXXXXX             XXXXX
#   XXXXXXXX

nivel = int(input("Nivel (entre 2 y 40): "))

for i in range(nivel+1):
    for b in range(i):
        print("*", end="")
    print()