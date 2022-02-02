def es_repetición(cadena):
    if cadena[:len(cadena) // 2] == cadena[len(cadena) // 2:len(cadena)]:
        return True
    return False

print(es_repetición("peapea"))
