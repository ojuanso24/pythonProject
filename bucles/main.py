nivel = int(input("Nivel (entre 2 y 40): "))

for i in range(nivel, 0, -1):

    for b in range(i):
        print("*", end="")

    for b in range(2*(nivel-i)):
        print(" ", end="")

    for b in range(i):
        print("*", end="")

    print()

for i in range(1, nivel+1):

    for b in range(i):
        print("*", end="")

    for b in range(2*(nivel-i)):
        print(" ", end="")

    for b in range(i):
        print("*", end="")

    print()