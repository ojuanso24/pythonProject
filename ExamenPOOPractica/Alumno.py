class Alumno:
    def __init__(self, nombre, edad = 18):
        self.nombre = nombre
        if type(edad) == int:
            self.edad = edad
        else:
            self.edad = 18
class Aula:
    def __init__(self, Ciclo = "DAM", Curso = 1):
        self.Ciclo = Ciclo
        self.Curso = Curso
        self.ListadoAlumnos = []

    def InsertarAlumnos(self, Alu):
        if type(Alu) == Alumno:
            if len(self.ListadoAlumnos) <= 30:
                self.ListadoAlumnos.append(Alu)
                print("Correcto")
            else:
                print("Aula llena")

    def ExisteAlumno(self, nombre):
        for i in self.ListadoAlumnos:
            if i.nombre == nombre:
                return True
        return False

    def AlumnosMenores(self):
        dic = {}
        for i in self.ListadoAlumnos:
            if i.edad < 18:
                if "menores" in dic:
                    dic["menores"].append(i.nombre)
                else:
                    dic["menores"] = [i.nombre]
            else:
                if i.edad in dic:
                    dic[i.edad].append(i.nombre)
                else:
                    dic[i.edad] = [i.nombre]
        return dic

    def __str__(self):
        salida = "Ciclo: " + self.Ciclo + "\nCurso: " + str(self.Curso) + "\nAlumnos: "
        for i in self.ListadoAlumnos:
            salida += i.nombre + ", "
        return salida[:-2]


opcion = input("1. Crear Alumno\n"
               "2. Crear Aula\n"
               "3. Insertar Alumno Aula\n"
               "4. Mostrar Todos\n"
               "5. Existe Alumno\n"
               "6. Insertar Alumnos Aula no repetidos\n"
               "7. Alumnos Menores\n"
               "8. Salir\n--> ")
while opcion != "8":
    if opcion == "1":
        nombre = input("Nombre del Alumno?: ")
        edad = input("Quieres intruducir la edad? (S)Si, Cualquier otra tecla no: ").lower() == "s" if True else False
        if edad:
            alumno = Alumno(nombre, int(input("Edad?: ")))
        else:
            alumno = Alumno(nombre)

    elif opcion == "2":
        ciclo = input("Quieres intruducir la ciclo? (S)Si, Cualquier otra tecla no: ").lower()
        if ciclo == "s":
            ciclo = input("Ciclo: ")
        else:
            ciclo = ""
        curso = input("Quieres intruducir la Curso? (S)Si, Cualquier otra tecla no: ").lower()
        if curso == "s":
            try:
                curso = int(input("Curso: "))
            except:
                print("Curso tiene que ser un numero")
                curso = ""
        else:
            ciclo = ""

        if ciclo != "":
            if curso != "":
                aula = Aula(ciclo, int(curso))
            else:
                aula = Aula(ciclo)
        elif curso != "":
            aula = Aula(Curso = curso)
        else:
            aula = Aula()

    elif opcion == "3":
        aula.InsertarAlumnos(alumno)

    elif opcion == "4":
        print(aula)

    elif opcion == "5":
        print(aula.ExisteAlumno(input("Nombre?: ")))

    elif opcion == "6":
        nombre = input("Nombre del Alumno?: ")
        if not aula.ExisteAlumno(nombre):
            edad = input("Quieres intruducir la edad? (S)Si, Cualquier otra tecla no: ").lower() == "s" if True else False
            if edad:
                alumno = Alumno(nombre, int(input("Edad?: ")))
            else:
                alumno = Alumno(nombre)

            aula.InsertarAlumnos(alumno)
        else:
            print("El alumno ya existe")
    elif opcion == "7":
        print(aula.AlumnosMenores())

    opcion = input("1. Crear Alumno\n"
                   "2. Crear Aula\n"
                   "3. Insertar Alumno Aula\n"
                   "4. Mostrar Todos\n"
                   "5. Existe Alumno\n"
                   "6. Insertar Alumnos Aula no repetidos\n"
                   "7. Alumnos Menores\n"
                   "8. Salir\n--> ")