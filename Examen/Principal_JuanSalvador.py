import Utilidades_JuanSalvador

numero = int(input("Intruduce el Tamaño de la Matriz: "))
nombre = input("Intruduce un nombre: ").lower().replace(" ", "")

miMatriz = Utilidades_JuanSalvador.GenerarMatriz(numero, nombre)

print("Matriz Original:")
Utilidades_JuanSalvador.MostrarMatriz(miMatriz)
Utilidades_JuanSalvador.Fastidiar(miMatriz, nombre)

print("\nMatriz Modificada:")
Utilidades_JuanSalvador.MostrarMatriz(miMatriz)
print()

if Utilidades_JuanSalvador.ComprobarResultado(miMatriz, nombre):
    print("La Matriz es correcta, está el nombre exactamente")
else:
    print("La Matriz no es correcta,no está bien el nombre")