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
    elif opcion == 3:
    elif opcion == 4:
    elif opcion == 5:
    else:
        print("Opcion no valida, seleccione un numero entre 1 y 5")