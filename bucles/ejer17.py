if __name__ == '__main__':
    # No queria usar metodos ya que son ejer de bucles solo, pero quedaria algo mas leíble
    repetir = True
    # Primer bucle para ver si quiere repetir
    while repetir:
        tramposo = False
        salir = False
        max = 101
        min = 0
        contador = 1
        print("Piense un número del 0 al 100 (no me engañe ni cambie de número")
        # bucle que contiene el programa principal
        while not salir:
            numero = (min + max)//2
            opcion = input("¿es el "+ str(numero) + "? (m-mayor, n-menor, i-igual) \n ")
            if opcion == "i":
                salir = True
            elif opcion == "m":
                # Miramos si miente
                if max < numero + 2:
                    salir = True
                    tramposo = True
                else:
                    min = (min + max)//2
                contador += 1
            elif opcion == "n":
                # Miramos si miente
                if min > numero - 1:
                    salir = True
                    tramposo = True
                else:
                    max = (min + max)//2
                contador += 1
        # Comprobamos que no es un tramposo e imprimimos segun el numero de aciertos
        if tramposo:
            print("tramposooooo")
        else:
            if contador <= 2:
                print("¡¡¡Qué bueno soy, lo he acertado en tan sólo", contador, "intentos!!!")
            if contador <= 4:
                print("¡¡¡Bien, lo he acertado en tan sólo", contador, "intentos!!!")
            if contador <= 6:
                print("Bien, lo he acertado en tan sólo", contador, "intentos!!!")
            if contador <= 8:
                print("Bueno no esta mal, lo he acertado en tan sólo", contador, "intentos!!!")
            else:
                print("El numero es", numero, "se acerto en", contador, "intento")

        #Bucle para asegurarse que pone la opcion correcta
        while opcion != "S" and opcion != "N":
            opcion = input("¿Desea jugar otra vez (S/N)? ")
            if opcion == "N":
                repetir = False