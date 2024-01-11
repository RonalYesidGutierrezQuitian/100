def calcularTotalPrestamo():
    # Declaración de variables
    monto = 1000.0
    intereses = 0.0
    total_pagar = 0.0
    meses = 0

    # Entrada de datos
    while True:
        try:
            print("Número de meses: ", end="")
            meses = int(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número entero.')

    # Proceso
    intereses = monto * (meses * 0.02)
    total_pagar = monto + intereses

    # Salida
    print("\nINTERESES      : ", intereses)
    print("TOTAL A PAGAR  : ", total_pagar)

# Llamada a la función principal
calcularTotalPrestamo()