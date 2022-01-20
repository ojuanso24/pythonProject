if __name__ == '__main__':
    contadorAlumnos = 0
    aprobados: int = 0
    suspensos = 0
    total = 0
    entrada = " "

    entrada = input("Nota del alumno " + str(contadorAlumnos + 1) + ": ")
    while entrada != '':
        try:
            nota = float(entrada)
            if nota >= 0 and nota <= 10:
                if nota < 5:
                    suspensos += 1
                else:
                    aprobados += 1
                contadorAlumnos += 1
                total += nota
            else:
                print("La nota no esta dentro del rango")
            entrada = input("Nota del alumno " + str(contadorAlumnos + 1) + ": ")
        except:
            print("Dato no valido")

    print("Número de alumnos: ", contadorAlumnos)
    print("Aprobados: ", aprobados)
    print("Suspensos: ", suspensos)
    print("Nota media: ", round(total / contadorAlumnos, 2))