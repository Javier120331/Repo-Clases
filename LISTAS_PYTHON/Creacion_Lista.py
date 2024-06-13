while True:
    try:
        Creacion_Lista = int(input("Desea Crear un Lista? \n 1. Si 2.No "))

        if Creacion_Lista == 1:
            serpList = []
            while True:
                try:
                    AgregadoLista = int(input("Desea Agregar algo a la Lista? \n 1.Si 2.No "))
                    if AgregadoLista == 1:
                        Texto_Agregado = input("Ingrese el Texto a Agregar")
                        serpList.append(Texto_Agregado)
                    else:
                        print("Saliendo Del programa...") 
                        print(f"Su lista es :{serpList}")
                        break 
                except ValueError as e:
                    print("La respuesta Debe ser 1 o 2  ")     
            break      
        elif Creacion_Lista == 2:
            print("Saliendo Del programa...")           
        else:
            print("Ingrese un numero valido")
        break    
    except ValueError as e:
        print("La respuesta Debe ser 1 o 2  ")       
        