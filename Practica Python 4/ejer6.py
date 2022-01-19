n1 = 0
n2 = 1
contador = 0
lista = []
while contador <= 50:
    lista.append(n1)
    lista.append(n2)
    n1 = n1 + n2
    n2 = n1 + n2
    contador += 1

print(lista)
