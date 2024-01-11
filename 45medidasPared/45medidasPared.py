def calcularMedidasPared():
    # Declaración de variables
    alto = 0
    largo = 0
    arena = 0.0

    # Entrada de datos
    while True:
        try:
            print("Ingrese alto de la pared en metros: ", end="")
            alto = int(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número entero.')

    while True:
        try:
            print("Ingrese largo de la pared en metros: ", end="")
            largo = int(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número entero.')

    # Proceso
    arena = (alto * largo) * 0.25

    # Salida
    print("\nArena Necesaria: {:.2f} m^3".format(arena))

# Llamada a la función principal
calcularMedidasPared()