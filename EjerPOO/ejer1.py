class COrdenador:
    def __init__(self, CMarca, CProcesador,  CPeso, CEstado, CPatantalla):
        self.CMarca = CMarca
        self.CProcesador = CProcesador
        self.CPeso = CPeso
        self.CEstado = CEstado
        self.CPatantalla = CPatantalla

    def encenderOdenador(self):
        if self.CEstado != "Encendido":
            print("No Encendido, Va a encenderse ahora...")
            self.CEstado = "Encendido"
            self.encenderPantalla()
            print("Ordenador Encendido ")
        else:
            print("Encendido")

    def apagarOdenador(self):
        if self.CEstado != "Apagado":
            self.CEstado = "Apagado"
            print("Ordenador Apagado")
        else:
           print("El ordenador esta ya apagado")

    def encenderPantalla(self):
        if self.CEstado != "Activa":
            self.CPatantalla = "Activa"
            print("Pantalla Activa")
        else:
            print("La pantalla esta ya Activa")

    def apagarPantalla(self):
        if self.CPatantalla != "Inactiva":
            self.CPatantalla = "Inactiva"
            print("Pantalla Apagada")
        else:
           print("La pantalla esta ya apagada")

    def __str__(self):
        return 'COrdenador:\n\tCMarca: {}\n\tCProcesador: {}\n\tCPeso: {}\n\tCEstado: {}\n\tCPatantalla: {}'.format(
            self.CMarca, self.CProcesador, self.CPeso, self.CEstado, self.CPatantalla)

Ordenadorcasa = COrdenador("HP", "I5", 6, "Apagado", "Inactiva")
Ordenadortrabajo = COrdenador("ASUS", "I7", 7, "Apagado", "Inactiva")
Ordenadortrabajo.encenderOdenador()
Ordenadorcasa.apagarOdenador()
# Ordenadortrabajo.estado()
print(Ordenadortrabajo)
print(Ordenadorcasa)
# Ordenadorcasa.estado()
Ordenadortrabajo.apagarPantalla()
# Ordenadortrabajo.estado()
print(Ordenadortrabajo)
Ordenadortrabajo.apagarOdenador()

