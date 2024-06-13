texto = input(" ingresa un texto: ")

palabras = texto.split()
diccionario = {}

for palabra in palabras:
    

    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print("\nFRECUENCIA DE CADA PAALABRA:")
for palabra, frec in diccionario.items():
    print(f"{palabra}: {frec}")