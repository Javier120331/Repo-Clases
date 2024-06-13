texto_sutro = input("Ingrese un texto sutriño")

palabras_sutras = texto_sutro.split()

Frecuencia_sutra = {}
for Palabra in palabras_sutras:
    Palabra = Palabra.lower()
    Frecuencia_sutra[Palabra] = Frecuencia_sutra.get(Palabra,0) + 1
    
    print("frecuencia De palabras sutras: ")
    for palabra, frecuencia in Frecuencia_sutra.items():
        print(f"{palabra}:{Frecuencia}")
