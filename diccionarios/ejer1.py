if __name__ == '__main__':
    diccionario = {}
    entrada = input("Entrada: ")
    for i in entrada:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1

    if " " in diccionario:
        del diccionario[' ']
    print(diccionario)