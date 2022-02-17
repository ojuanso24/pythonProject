class Diccionario:
    def __init__(self, nombre, editorial, nivel):
        self.nombre = nombre
        self.editorial = editorial
        self.nivel = nivel
        self.diccionario = {}

    def anadirPalabra(self, palabra):
        letra = palabra[0:1]
        print(letra)
        if letra in self.diccionario:
            if not palabra in self.diccionario[letra]:
                self.diccionario[letra][palabra] = []
            else:
                print("Palabra ya añadida")
        else:
            self.diccionario[letra] = {palabra: []}

    def palabraExiste(self, palabra):
        letra = palabra[0:1]
        if letra in self.diccionario:
            if palabra in self.diccionario[letra]:
                return True;
            else:
                return False;
        else:
            return False;

    def anadirAcepciones(self, palabra, acepcion):
        if self.palabraExiste(palabra):
            self.diccionario[palabra[0:1]][palabra].append(acepcion)
        else:
            print("Palabra no encontrada")

    def consultarPalabra(self, palabra):
        letra =palabra[0:1]
        if self.palabraExiste(palabra):
            for i in self.diccionario[letra][palabra]:
                 print(i)
        else:
            print("Palabra no encontrada")

    def consultarLetra(self, letra):
        if self.palabraExiste(letra):
            for i in self.diccionario[letra]:
                 print(i)
        else:
            print("Palabra no encontrada")

opcion = input("1)Crear diccionario\n"
               "2)Introduce palabras\n"
               "3)Introduce Acepciones\n"
               "4)Consultar palabra y acepciones\n"
               "5)Enseñar palabra por letra indicada\n"
               "6)Salir\n")
while opcion != 6:
    if opcion == "1":
        diccionario = Diccionario(input("nombre?: "), input("editorial?: "), input("nivel?: "))
    elif opcion == "2":
        diccionario.anadirPalabra(input("palabra?: ").lower())
    elif opcion == "3":
        diccionario.anadirAcepciones(input("palabra?: "), input("acepcion?: "))
    elif opcion == "4":
        diccionario.consultarPalabra(input("palabra?: "))
    elif opcion == "5":
        diccionario.consultarLetra(input("letra?: "))
    opcion = input("1)Crear diccionario\n"
                   "2)Introduce palabras\n"
                   "3)Introduce Acepciones\n"
                   "4)Consultar palabra y acepciones\n"
                   "5)Enseñar palabra por letra indicada\n"
                   "6)Salir\n")
print("Fin")
