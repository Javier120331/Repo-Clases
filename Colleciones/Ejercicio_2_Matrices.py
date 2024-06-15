# Crear un arreglo [3][3][3] manuelmente,
# los valores del arreglo pueden ser 
# "amarrilo" "rojo" "naranja" "verde" "blanco" 
# Una vez completado, mostrar la siguiente informacion:


arreglo = [
    
    ["amarillo", "rojo", "verde"],
    ["rojo", "rojo", "verde"], 
    ["verde", "rojo", "verde"]
]
[
    ["amarillo", "rojo", "verde"],
    ["amarillo", "rojo", "verde"],
    ["amarillo", "rojo", "verde"]
    
]
[
    ["amarillo", "rojo", "verde"],
    ["amarillo", "rojo", "verde"],
    ["amarillo", "rojo", "verde"]
    
]

#Contador
contadores = {
    "amarillo": 0,
    "rojo": 0,
    "verde": 0,
}



#iterar el arreglo

for i in range(3):
    for j in range(3):
        for k in range(3):
            elemento = arreglo[i][j][k]
            if elemento in contadores:
                contadores[elemento] += 1
                
#printear contadores                
print("Número de elementos 'amarillo':", contadores["amarillo"])
print("Número de elementos 'rojo':", contadores["rojo"])
print("Número de elementos 'verdes':", contadores["verde"])

