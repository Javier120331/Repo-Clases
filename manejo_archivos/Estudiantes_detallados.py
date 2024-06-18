import csv




Lista_diccionario = []

with open("alumnos_detallado.csv", "r", newline="", encoding="utf-8") as archivo:
    datos_leidos = csv.reader(archivo)

    for i in datos_leidos:
        print(i)