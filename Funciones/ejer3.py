import re

def es_nif(NIF):
    if re.match("[0-9]{8}[A-Z]", NIF) and len(NIF) == 9:
        letra = NIF[-1]
        numero = int(NIF.split(letra)[0])
        numerosLetras = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                         11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C",
                         21: "K", 22: "E"}
        if letra == numerosLetras[numero % 23]:
            return True
    return False

print(es_nif("09065050Z"))