import random

palabras = ["pelota", "coche"]

palabra = list(palabras[random.randint(0, len(palabras) - 1)])

palabraOculta = ["-"] * (len(palabra))
tablero = [" ---------|  \n"
           " |       ###  \n"
           " |       ###  \n"
           " |        |   \n"
          f" |        |     {palabraOculta}\n"
           " |        |      \n"
           " |            \n"
           " |           \n"
           " |            \n"
           " |               \n"
           " ---             \n",

           " ---------|  \n"
           " |       ###  \n"
           " |       ###  \n"
           " |        |   \n"
          f" |     ---|     {palabraOculta}\n"
           " |        |      \n"
           " |             \n"
           " |             \n"
           " |             \n"
           " |               \n"
           " ---             \n",

           " ---------|  \n"
           " |       ###  \n"
           " |       ###  \n"
           " |        |   \n"
          f" |     ---|---  {palabraOculta}\n"
           " |        |      \n"
           " |             \n"
           " |             \n"
           " |             \n"
           " |               \n"
           " ---             \n",

           " ---------|  \n"
           " |       ###  \n"
           " |       ###  \n"
           " |        |   \n"
          f" |     ---|---  {palabraOculta}\n"
           " |        |      \n"
           " |       /      \n"
           " |      /       \n"
           " |     /        \n"
           " |               \n"
           " ---             \n",

           " ---------|  \n"
           " |       ###  \n"
           " |       ###  \n"
           " |        |   \n"
          f" |     ---|---  {palabraOculta}\n"
           " |        |      \n"
           " |       / \    \n"
           " |      /   \    \n"
           " |     /     \   \n"
           " |               \n"
           " ---             \n"
           ]
errores = 0
while palabraOculta != palabra and errores < len(tablero) -1 :
    c = input("a:")
    acertada = False
    for i in range(len(palabra)):
        if c == palabra[i]:
            palabraOculta[i] = palabra[i]
            acertada = True

    if not acertada:
        errores += 1

    print(tablero[errores])
    print(palabraOculta, errores, palabra)

