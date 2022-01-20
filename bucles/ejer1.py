if __name__ == '__main__':
    try:
        numero = int(input("Número: "))
        contador = 0
        while contador <= 10:
            print(numero, "x", contador, "=", numero * contador)
            contador += 1

        print("--------")
        for i in range(11):
            print(numero, "x", i, "=", numero * i)
    except:
        print("Dato no valido")