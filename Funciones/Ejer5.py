def dia_agno(dia, mes, agno):
    anos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (agno % 4 == 0 and agno % 100 != 0) or (agno % 4 == 0 and agno % 400 == 0):
        anos[1] = 29

    for i in range(mes -1):
        dia += anos[i]

    return dia

print(dia_agno(21, 5, 200))