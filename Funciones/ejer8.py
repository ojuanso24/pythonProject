def muestra_nota_de_alumnos(listaNombre, listaNotas, alumnoBuscado):
    for i in range(len(listaNombre)):
        if listaNombre[i] == alumnoBuscado:
            return [alumnoBuscado, listaNotas[i]]
    return None


def nombres_aprobados(listaNombre, listaNotas):
    listaAprobados = []
    for i in range(len(listaNombre)):
        if listaNotas[i] >= 5:
            listaAprobados.append(listaNombre[i])
    return listaAprobados


def nombres_mejor_nota(listaNombre, listaNotas):
    listaMejorNota = []
    mejorNota = max(listaNotas)
    for i in range(len(listaNombre)):
        if listaNotas[i] == mejorNota:
            listaMejorNota.append(listaNombre[i])
    return listaMejorNota


def superior_igual_nota_media(listaNombre, listaNotas):
    listaMayorMedia = []
    media = sum(listaNotas) / len(listaNotas)
    for i in range(len(listaNombre)):
        if listaNotas[i] >= media:
            listaMayorMedia.append(listaNombre[i])
    return listaMayorMedia


def muestra_solo_nota_de_alumnos(listaNombre, listaNotas, alumnoBuscado):
    for i in range(len(listaNombre)):
        if listaNombre[i] == alumnoBuscado:
            return  listaNotas[i]
    return None


listaNombre = ["juan", "ana", "jose", "pepe", "pablo", "andres"]
listaNotas = [1, 5, 6, 2, 9, 9]
print(muestra_nota_de_alumnos(listaNombre, listaNotas, "pablo"))
print(nombres_aprobados(listaNombre, listaNotas))
print(nombres_mejor_nota(listaNombre, listaNotas))
print(superior_igual_nota_media(listaNombre, listaNotas))
print(muestra_solo_nota_de_alumnos(listaNombre, listaNotas, "pablo"))