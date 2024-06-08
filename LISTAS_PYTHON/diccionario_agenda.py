datos = []

lista = []

for i in range(2):
    
nombre = input("ingrese Nombre:")
direccion = input("ingrese Direccion: ")
Telefono = input("ingrese Telefono: ")
Email = input("ingrese email: ")
Estado = input("ingrese Estado:")
datos[nombre] = {
    "direccion": direccion,
    "Telefono": Telefono,
    "Email": Email,
    "Estado": Estado}