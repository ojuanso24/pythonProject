if __name__ == '__main__':
    mayor = 0
    entrada = float(input("Introduzca un número (cero para terminar): "))
    mayor = entrada

    while entrada != 0:
        try:
            entrada = float(input("Introduzca un número (cero para terminar): "))
            if entrada >= mayor:
                mayor = entrada
        except:
            print("Dato no valido")
    print("Mayor:", mayor)
