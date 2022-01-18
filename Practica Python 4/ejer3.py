if __name__ == '__main__':
    suspensos = 0
    aprobados = 0
    listaNotas = []
    contador = 0
    print("Introduce las notas. ENTER para terminar: ")
    entrada = input("Nota del alumno " + str(contador + 1) + ": ")
    while entrada != "":
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                if nota < 5:
                    suspensos += 1
                else:
                    aprobados += 1
                contador += 1
                listaNotas.append(nota)
            else:
                print("Nota fuera de rango")
        except:
            print("Dato no valido")

        entrada = input("Nota del alumno " + str(contador + 1) + ": ")

    print("Se han introducido las siguientes notas:")
    total = 0
    for i in range(len(listaNotas)):
        print("\tAlumno", i + 1, ": ", listaNotas[i])
        total += listaNotas[i]

    print("Resumen")
    print("\tNúmero de alumnos:", contador)
    print("\tAprobados:", aprobados)
    print("\tSuspensos:", suspensos)
    print("\tNota media:", total / contador)

