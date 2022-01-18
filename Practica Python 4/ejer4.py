if __name__ == '__main__':
    try:
        lista = []
        entrada = input("Introduce nombres. ENTER para terminar: ")
        while entrada != "":
            lista.append(entrada)
            entrada = input("Introduce nombres. ENTER para terminar: ")
        lista.sort()
        print("Los nombres son:")
        for i in lista:
            print(i)
    except:
        print("Dato no valido")