def calcularCostoTotal():
    # Declaración de variables
    h = 0
    m = 0
    s = 0
    costo = 0.0

    # Entrada de datos
    while True:
        try:
            print("HORAS     : ", end="")
            h = int(input())
            print("MINUTOS   : ", end="")
            m = int(input())
            print("SEGUNDOS  : ", end="")
            s = int(input())
            break
        except ValueError:
            print('Datos inválidos. Ingrese números enteros.')

    # Proceso
    costo = ((h * 3600) + (m * 60) + s) * 0.25

    # Salida
    print("\nCOSTO TOTAL : {:.2f}".format(costo))

# Llamada a la función principal
calcularCostoTotal()