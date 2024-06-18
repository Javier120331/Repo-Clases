import csv
import json
#abrir archivo, r permiso de lectura
with open("archivo.json", "r") as archivo:
    datos_leidos = json.load(archivo)
    for i in datos_leidos:
        print(i)
    
   


datos = {}
datos["nombre"] = {}
datos["nombre"]["nota1"] = 54