if __name__ == '__main__':
    try:
        total = 0
        numero = int(input("Introduzca un número: "))
        if numero > 0:
            for i in range(0, numero + 1, 2):
                total += i
            print("La suma es:", total)
        else:
            print("Tiene que se un número +")
    except:
        print("Dato no valido")