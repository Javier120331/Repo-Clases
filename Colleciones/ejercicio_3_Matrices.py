#Crear un Arreglo [10][4] en el cual simula un bus, tendrá que darle de forma
#automática los números de asiento y luego mostrarlo por pantalla
#de la siguiente forma
#1 2 3 4

# Crear un arreglo [10][4] para simular los asientos del bus
filas = 10
columnas = 4
contador_asiento = 1
arreglo_bus = []

# Asignar números de asiento automáticamente y construir el arreglo
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(contador_asiento)
        contador_asiento += 1
    arreglo_bus.append(fila)

# Mostrar el arreglo por pantalla en el formato solicitado
for fila in arreglo_bus:
    for asiento in fila:
        print(asiento, end=" ")
    print()  # Salto de línea después de cada fila

