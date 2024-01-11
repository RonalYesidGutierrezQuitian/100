def calcularHorasMinutosSegundos():
    # Declaración de variables
    xseg = 0
    hor = 0
    min = 0
    seg = 0

    # Entrada de datos
    while True:
        try:
            print("Ingrese la cantidad de segundos: ", end="")
            xseg = int(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número entero.')

    # Proceso
    hor = int(xseg / 3600)
    min = int((xseg - (hor * 3600)) / 60)
    seg = int(xseg - ((hor * 3600) + (min * 60)))

    # Salida
    print("\nHORAS    : ", hor)
    print("MINUTOS  : ", min)
    print("SEGUNDOS : ", seg)

# Llamada a la función principal
calcularHorasMinutosSegundos()