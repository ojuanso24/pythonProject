if __name__ == '__main__':
    try:
        numero = int(input("Número: "))
        if numero % 2 == 0:
            for i in range(1,numero + 1):
                print(" " * (numero - i) + "X" * (2 * i))

        if numero % 2 != 0:
            for i in range(numero):
                print(" " * (numero - i - 1) + "X" * (2 * i + 1))
    except:
        print("Datos no valido")