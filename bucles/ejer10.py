import random

if __name__ == '__main__':
    cero_diecinueve = 0
    veinte_treintaynueve = 0
    cuarenta_cincuentaynueve = 0
    sesenta_setentaynueve = 0
    ochenta_noventaynueve = 0

    for i in range(100):
        numero = random.randint(0,99)
        if 0 <= numero <= 20:
            cero_diecinueve += 1
        elif numero <= 40:
            veinte_treintaynueve += 1
        elif numero <= 60:
            cuarenta_cincuentaynueve += 1
        elif numero <= 80:
            sesenta_setentaynueve += 1
        elif numero <= 100:
            ochenta_noventaynueve += 1

    print("[ 0-19]:", cero_diecinueve, "\n[20-39]:", veinte_treintaynueve, "\n[40-59]:", cuarenta_cincuentaynueve, "\n[60-79]:", sesenta_setentaynueve, "\n[80-99]:", ochenta_noventaynueve, end=' ')