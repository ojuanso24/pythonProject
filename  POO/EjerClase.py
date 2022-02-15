from builtins import input


class Productos():
    def __init__(self, referencia="A1", tipo="pelicula"):
        self.referencia = referencia
        self.tipo = tipo
        self.alquilado = False

    def anadirProductos(self):
        pass

    def mostrar(self):
        cadena = "\tProducto " + self.referencia
        cadena += "\n\tTipo: " + self.tipo
        cadena += "\t\nAlquiler: " + "Si" if self.alquilado else "No" + "\n"
        return cadena


class Videoclub():
    def __init__(self, Nombre = "DAM"):
        self.Nombre = Nombre
        self.Poductos = dict()

    def listadoProductos(self):
        cadena = "Productos Videoclub \n"
        for p in self.Poductos:
            cadena += self.Poductos[p].mostar()
        return cadena

    def fichproducto(self, referencia):
        return self.Poductos[referencia].mostrar()

miVideoclub = Videoclub()
opcion = input("1-Listar, 8-Salir :")
while opcion != "8":
    if opcion == "1":
        ref = input("Referencia: ")
        tipo = input("Tipo: ")
        miVideoclub.anadirProductos(ref, tipo)
    elif opcion == "2":
        print(miVideoclub.listadoProductos())
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        pass
    elif opcion == "7":
        pass
    opcion = input("1-Listar, 8-Salir :")
