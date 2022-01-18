if __name__ == '__main__':
    try:
        salida = ""
        contador = 0
        billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        dinero = int(input("Introduzca una cantidad: "))
        while dinero > 0:
            if billetes_monedas[contador] <= dinero:
                entero = int(dinero / billetes_monedas[contador])
                dinero = dinero % billetes_monedas[contador]
                if entero != 0:
                    if billetes_monedas[contador] > 2:
                        if entero == 1:
                            salida += str(entero) + " billete de " + str(billetes_monedas[contador])
                        else:
                            salida += str(entero) + " billetes de " + str(billetes_monedas[contador])
                        # salida += " " +entero + "billete de " + billetes_monedas[contador] + "\n"
                    else:
                        if entero == 1:
                            salida += str(entero) + " moneda de " + str(billetes_monedas[contador])
                        else:
                            salida += str(entero) + " monedas de " + str(billetes_monedas[contador])
                    salida += "\n"
                    entero = 0
            contador += 1
        print(salida)
    except:
        print("Datos no valido")