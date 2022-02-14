class hola:
    edad = 1
    apellido = None
    casa = "si"

    def salida(self, mensa):
        return 'edad: {}, apellido: {}, casa: {}, mensa: {}'.format(self.edad, self.apellido, self.casa, mensa)

    def __str__(self):
        return 'edad: {}, apellido: {}, casa: {}'.format(self.edad, self.apellido, self.casa)


hola = hola()
# dice si existe un parametro en el objeto
print('hola?', hasattr(hola, 'edad'))
print('hola?', hasattr(hola, 'apellido'))
print('hola?', hasattr(hola, 'apellido2'))  # no tiene ese atributo

print(hola)
print(hola.salida("Mensa de prueba"))
