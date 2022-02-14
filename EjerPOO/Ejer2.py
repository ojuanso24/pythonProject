class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.arrancado = False

    def ArrancarMotor(self):
        if not self.arrancado:
            print("Arrancamo el motor")