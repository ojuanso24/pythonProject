if __name__ == '__main__':
    try:
        numero = int(input("Número: "))
        if numero % 2 == 0:
            print("X" * (numero * 2))
            for i in range(1,numero , 1):
                print("X" * (numero - i) + " " * (2 * i) + "X" * (numero - i))

            for i in range(numero - 1, 0, -1):
                print("X" * (numero - i) + " " * (2 * i) + "X" * (numero - i))
            print("X" * (numero * 2))

        if numero % 2 != 0:
            print("X" * ((numero * 2) - 1))
            for i in range(numero - 1 ):
                print("X" * (numero - i - 1) + " " * (2 * i + 1) + "X" * (numero - i - 1))
            for i in range(numero - 2 , -1, -1):
                print("X" * (numero - i - 1) + " " * (2 * i + 1) + "X" * (numero - i - 1))
            print("X" * ((numero * 2) - 1))
    except:
        print("Datos no valido")