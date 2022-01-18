if __name__ == '__main__':
    try:
        dias = int(input("Número de días del mes: "))
        primerDia = int(input("Día 1 es (0 lunes, 6 domingo): "))
        if primerDia >= 0 and primerDia <= 6:
            contador = primerDia
            print(" L", " M", " X", " J", " V", " S", " D")
            for i in range(primerDia):
                print("", " ", end=" ")

            for i in range(dias):
                if contador == 7:
                    print()
                    contador = 0

                if len(str(i + 1)) == 1:
                    print("", i + 1, end=" ")

                if len(str(i + 1)) == 2:
                    print(i + 1, end=" ")
                contador += 1
        else:
            print("Número fuera de rango")
    except:
        print("Datos no valido")