class Mueble:
    def __init__(self, tipo):
        self.tipo = tipo
        self.__privada = "Privado"
        self.publica = "Publica"
    def getPrivada(self):
        return self.__privada

class Mesa(Mueble):
    def __init__(self, tipo, color):
        Mueble.__init__(self, tipo)
        self.color = color



mu = Mueble(3)
print(mu.tipo)
print(mu.publica)
print(mu.getPrivada())
print(mu._Mueble__privada) #acceder a una propiedad privada