class Empleado:
    def __init__(self, nombre = "", edad = 18, salario = 100):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def mostrarClasificación(self):
        if self.edad <= 21:
            print("Principiante")
        elif self.edad <= 35:
            print("Medio")
        elif self.edad > 35:
            print("Senior")

    def aumentraSalario(self, porcentaje):
        self.salario = porcentaje / 100 * self.salario + self.salario

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSalario: {self.salario}\n"


class Porgramador(Empleado):
    def __init__(self, nombre="pro", edad = 40, salario = 1000, lineasDeCodigoPorHora= 50, lenguajeDominante = "java"):
        super().__init__(nombre, edad, salario)
        self.lineasDeCodigoPorHora = lineasDeCodigoPorHora
        self.lenguajeDominante = lenguajeDominante

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSalario: {self.salario}\nlineasDeCodigoPorHora: {self.lineasDeCodigoPorHora} " \
               f"\nlenguajeDominante: {self.lenguajeDominante}\n"

lista = []
opcion = input("1. Crear Empleado\n"
                "2. Crear Porgramador\n"
                "3. AumentraSalario\n"
                "4. Mostrar Todos\n"
                "5. Salir\n")

while opcion != "5":
    if opcion == "1":
        lista.append(Empleado())
    elif opcion == "2":
        lista.append(Porgramador())
    elif opcion == "3":
        lista[int(input("Posicion lista: "))].aumentraSalario(int(input("% aumento?: "))) # para no implemnetar un metodo bucar y poder hacer pruebas
    elif opcion == "4":
        for i in lista:
            print(i)
    opcion = input("1. Crear Empleado\n"
                   "2. Crear Porgramador\n"
                   "3. AumentraSalario\n"
                   "4. Mostrar Todos\n"
                   "5. Salir\n")
