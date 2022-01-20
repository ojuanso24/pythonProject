opcion = 0
coches = {}
max = 20
opcion = input("1.-Altas coche.\n2.-Baja coche.\n3.-Listar coches\n4.-Salir\nElija"
               " opción (1-4): ")
while opcion != "4":
    if opcion == "1":
        if len(coches) < max:
            caracteristicas = {"Marca": input("Marca?: "), "Modelo": input("Modelo?: ")}
            if not caracteristicas["Marca"] + caracteristicas["Modelo"] in coches:
                caracteristicas.update({"Cilindrada": input("Cilindrada?: "), "Potencia": input("Potencia?: "),
                                                                    "Velocidad Maxima": input("Velocidad Maxima?: ")})
                coches[caracteristicas["Marca"] + caracteristicas["Modelo"]] = caracteristicas
                print("Añadido", caracteristicas)
            else:
                print("Ya esta dentro")
        else:
            print("Ya tienes", max,"coches")
    elif opcion == "2":
        caracteristicas = {"Marca": input("Marca?: "), "Modelo": input("Modelo?: ")}
        if caracteristicas["Marca"] + caracteristicas["Modelo"] in coches:
            del coches[caracteristicas["Marca"] + caracteristicas["Modelo"]]
            print("Eliminado")
        else:
            print("No encontrado")
    elif opcion == "3":
        for i in coches:
            print(caracteristicas[i])
    else:
        print("Opción no valida")
    print("=====================")
    opcion = input("1.-Altas coche.\n2.-Baja coche.\n3.-Listar coches\n4.-Salir\nElija opción (1-4): ")
print(coches)
