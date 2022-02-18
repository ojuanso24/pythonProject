class Almacen:
    def __init__(self, Nombre = "Murcia"):
        self.Nombre = Nombre
        self.Productos = {}
        self.__Stock_Minimo = 0

    def ComparaProducto(self, nombreProducto, categoria, cantidad):
        if nombreProducto in self.Productos:
            self.Productos[nombreProducto][1] += cantidad # posible llamada a __setMinimo() preguntar
        else:
            self.Productos[nombreProducto] = [categoria]
            self.Productos[nombreProducto].append(cantidad)

    def VenderProducto(self, nombreProducto, categoria, cantidad):
        salida = ""
        if nombreProducto in self.Productos:
            if self.Productos[nombreProducto][1] >= cantidad:
                self.Productos[nombreProducto][1] -= cantidad
                return "Vendido"
            else:
                salida += f"La cantidad de {nombreProducto} en nuestro Almacén es: {self.Productos[nombreProducto][1]}"
        else:
            salida += "No existe el Producto en nuestro Almacén"

        listaKeys = list(self.Productos)

        contador = 0

        while contador < len(self.Productos) and (self.Productos[listaKeys[contador]][0] != categoria or self.Productos[listaKeys[contador]][1] < cantidad):
            # print(self.Productos[listaKeys[contador]][0], categoria, self.Productos[listaKeys[contador]][1], cantidad)
            contador += 1

        if contador < len(self.Productos) - 1:
            salida += f"\nTe recomendamos el producto: {listaKeys[contador]}"

        return salida

    def __str__(self):
        dicAux = {}
        salida = f"Almacen: {self.Nombre}\n"
        for i in self.Productos:
            if self.Productos[i][0] in dicAux:
                dicAux[self.Productos[i][0]] += "\n\t"+str(i) + ": " + str(self.Productos[i][1])
            else:
                dicAux[self.Productos[i][0]] = "\t" + str(i) + ": " + str(self.Productos[i][1])

        for j in dicAux:
            salida += str(j) + "\n" + dicAux[j] + "\n"

        return salida

    def __setMinimo(self, cantidad):
        if cantidad < 0:
            self.__Stock_Minimo = 0
        elif cantidad > 10:
            self.__Stock_Minimo = 10
        else:
            self.__Stock_Minimo = cantidad
        print("ADVERTENCIA: Productos por debajo del Strock Mínimo:")
        for i in self.Productos:
            if self.Productos[i][1] < self.__Stock_Minimo:
                print(f"\t{i}: {self.Productos[i][1]}")

    def __getMinimo(self):
        return self.__Stock_Minimo

    Minimo = property(__getMinimo, __setMinimo)


almacen = Almacen()
opcion = input("0)Salir\n"
               "1)Comprar Producto\n"
               "2)Vender Producto\n"
               "3)Mostrar Producto\n"
               "4)Actualizar Stock Mínimo\n--> ")
while opcion != "0":
    if opcion == "1":
        almacen.ComparaProducto(input("Nombre del producto: "), input("Categoria del producto: "), int(input("Cantidad de producto: ")))
    elif opcion == "2":
        print(almacen.VenderProducto(input("Nombre del producto: "), input("Categoria del producto: "),int(input("Cantidad de producto: "))))
    elif opcion == "3":
        print(almacen)
    elif opcion == "4":
        almacen.Minimo = int(input("Cantidad stock minimo: "))

    opcion = input("\n0)Salir\n"
                   "1)Comprar Producto\n"
                   "2)Vender Producto\n"
                   "3)Mostrar Producto\n"
                   "4)Actualizar Stock Mínimo\n--> ")

# almacen.ComparaProducto("Camion", "Jueguetes", 4)
# almacen.ComparaProducto("Muñeca", "Jueguetes", 2)
# almacen.ComparaProducto("Pantalon", "Ropa", 3)
# almacen.ComparaProducto("Pelota", "Jueguetes", 6)
# almacen.ComparaProducto("Ordenador", "Informática", 5)
# almacen.ComparaProducto("Monitor", "Informática", 5)
#
# almacen.Minimo = 4
#
# print(almacen)
# print(almacen.VenderProducto("Camion", "Jueguetes", 6))
