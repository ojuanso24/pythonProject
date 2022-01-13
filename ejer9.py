import math

if __name__ == '__main__':
    opcion = 0
    while opcion != 4:
        try:
            opcion = int(input("Cálculo de superficies: \n1.-Cuadrados\n2.-Triángulos\n3.-Círculos\n4.-Salir\nElija"
                               " opción (1-4): "))
            if opcion == 1:
                lado = float(input("Lado: "))
                print("La superficie es de", lado * lado, "cm²")
            elif opcion == 2:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("La superficie es de", base * altura, "cm²")
            elif opcion == 3:
                radio = float(input("Radio: "))
                print("La superficie es de", math.pi * (radio * radio), "cm²")
            elif opcion == 4:
                continue
            else:
                print("Opción no valida")
            print("=====================")
        except:
            print("Error")