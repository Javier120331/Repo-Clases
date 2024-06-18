import json

datos_json = []

with open("archivo.json", "r" , newline="", encoding= "utf-8" ) as archivo:
    datos_leidos = json.load(archivo)
    for i in datos_leidos:
        datos_json.append(i)
       


asistencias = [] 

for i in datos_json:
    if i["asistencia_final"] == "asistencia_final":
        continue
    asistencias.append((int(i["asistencia_final"])))

print(f"Asistencias : {asistencias}") 
promedio_asistencias = round(sum(asistencias) / len(asistencias),2)
print(promedio_asistencias)



