def calcularGananciasGarita():
    try:
        cantidad_vehiculos = int(input('Ingrese la cantidad de vehículos: '))
    except ValueError:
        print('Entrada inválida. Debe ingresar un número entero.')
        return

    total_manana = 0
    total_noche = 0
    total_bus = 0
    total_van = 0
    total_micro = 0

    for cont in range(1, cantidad_vehiculos + 1):
        print(f'>> TIPO DE VEHÍCULO Nro {cont}/{cantidad_vehiculos} : ')
        print("1. Ómnibus")
        print("2. Minivan")
        print("3. Micro")

        try:
            tipo_vehiculo = int(input("OPC: "))
        except ValueError:
            print('Entrada inválida. Debe ingresar un número entero.')
            return

        if tipo_vehiculo == 1:
            tarifa = 13
            total_bus += tarifa
        elif tipo_vehiculo == 2:
            tarifa = 10
            total_van += tarifa
        elif tipo_vehiculo == 3:
            tarifa = 8
            total_micro += tarifa

        turno = input("TURNO (M/N): ").upper()

        if turno == "M":
            total_manana += tarifa
        else:
            total_noche += tarifa

        print(" ")

    print("\nIMPORTE DE TURNO MAÑANA :", total_manana)
    print("IMPORTE DE TURNO NOCHE   :", total_noche)
    print("\nIMPORTE DE ÓMNIBUS       :", total_bus)
    print("IMPORTE DE MINIVAN        :", total_van)
    print("IMPORTE DE MICRO          :", total_micro)

# Llamada a la función principal
calcularGananciasGarita()