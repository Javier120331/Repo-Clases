#Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
#una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
#caracteres en un mensaje de salida por pantalla

Lista = []
NombreMayor = ""
for i in range(3):
   nombre = input("Ingrese un nombre")
   Lista.append(nombre)
   if len(NombreMayor) < len(nombre):
            mayor = nombre
            
print(mayor)    