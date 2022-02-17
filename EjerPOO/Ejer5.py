import random

class Asignatura:
    def __init__(self, nombre="SGE", nota=8):
        self.nombre = nombre
        self.__nota = nota

    def estado(self):
        if self.nota >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

    def __getNota(self):
        return self.__nota

    def __setNota(self, nota):
        self.__nota = nota

    nota = property(__getNota, __setNota)

    def getNombre(self):
        return self.nombre


class Alumno:
    def __init__(self, nombre="Pepe", edad=18):
        self.__nombre = nombre
        self.__edad = edad
        self.asignaturas = []

    def anadirAsignatura(self, Asignatura):
        if not Asignatura in self.asignaturas:
            self.asignaturas.append(Asignatura)
        else:
            print("La asignatura ya esta añadida")

    def __getNombre(self):
        return self.__nombre

    def __setNombre(self, nombre):
        self.__nombre = nombre

    def __getEdad(self):
        return self.__edad

    def __setEdad(self, edad):
        self.__edad = edad

    nombre = property(__getNombre, __setNombre)
    edad = property(__getEdad, __setEdad)

listaAlumnos = [Alumno(), Alumno("Luis"), Alumno("Juan", 20)]
for i in listaAlumnos:
    i.anadirAsignatura(Asignatura("Lengua", random.randint(0, 100)))
    i.anadirAsignatura(Asignatura("Mates", random.randint(0, 100)))
    i.anadirAsignatura(Asignatura("Fisica", random.randint(0, 100)))
    i.anadirAsignatura(Asignatura("Naturales", random.randint(0, 100)))

for alu in listaAlumnos:
    print(f"Nombre Alumno: {alu.nombre} \nEdad: {alu.edad}")
    total = 0
    contador = 0
    for asignatura in alu.asignaturas:
        total += asignatura.nota
        contador += 1
        print(f"Asignatura: {asignatura.nombre}, nota: {asignatura.nota}, Estado: {asignatura.estado()}")
    print("Media: " + str(total / contador))