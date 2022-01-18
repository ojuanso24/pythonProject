if __name__ == '__main__':
    entrada = ''
    while entrada != 0:
        try:
            if entrada == '':
                entrada = float(input("Introduzca un número (cero para terminar): "))
                mayor = entrada
            else:
                entrada = float(input("Introduzca un número (cero para terminar): "))
                if entrada >= mayor:
                    mayor = entrada
        except:
            print("Dato no valido")
    print("Mayor:", mayor)