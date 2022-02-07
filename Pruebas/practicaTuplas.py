from builtins import tuple

mitupla = ("Juan", 1 ,3, "Juan", 1)
miLista = list(mitupla)
mitupla2 = tuple(miLista)

print(mitupla, miLista, mitupla2, mitupla[1:])
print("Juan" in mitupla) #si esta dentro
print(len(mitupla))
print(mitupla.count("Juan")) #cuenta las repetidas

nombreFecha = ("pepe", 13, 1, 2000)
nombre, dia, mes, anio = nombreFecha
print(nombre, dia, mes ,anio)