
arreglo = []



for i in range(3):
    fila = []
    for j in range(4):
        elemento = input(f"ingrese elemento para la posicion [{i}][{j}]")
        fila.append(elemento)
    arreglo.append(fila)    
print(arreglo)    