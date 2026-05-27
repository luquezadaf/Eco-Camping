capacidad_maxima = 15
sitios_ocupados = 0
sitios_libres = 0
ejecutando = True

while ejecutando:

    print("\n===Bienvenido a Eco Campings===")
    print("1. Conocer capacidad disponible")
    print("2. Entrada de vehiculos")
    print("3. Salida de vehiculos")
    print("4. Estado actual del camping")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese opción a realizar: "))
    except ValueError:
        print("Opcion no valida, por favor ingrese un numero entre 1 y 5")
        continue
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"Actualmente hay {disponibles} sitios disponibles")
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0:
            print("Lo sentimos, no quedan espacios en el camping")
        else:
            try:
                ingreso = int(input("¿Cuantos sitios o vehiculos van a ingresar?"))
                if ingreso <= 0:
                    print("Error: La cantidad debe ser mayor a 0")
                elif ingreso > sitios_libres:
                    print(f"Solo puede ingresar un máximo de {sitios_libres} sitios libres")
                else:
                    sitios_ocupados += ingreso
                    print(f"Ingreso registrado. Se han ocupado {ingreso} de sitios")
            except ValueError:
                print("Error: debe ingresar un número valido")
    elif opcion == 3:
        
    elif opcion == 4:
    elif opcion == 5:
    else:
        print("Opcion no valida, seleccione un numero entre 1 y 5")