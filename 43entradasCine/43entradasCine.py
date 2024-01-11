def calcularEntradasCine():
    # Declaración de variables
    monto = 0.0
    cant = 0

    # Entrada de datos
    while True:
        try:
            print("Ingrese la cantidad de dinero: $", end="")
            monto = float(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número.')

    # Proceso
    cant = round(monto / 15)

    # Salida
    print("\nNúmero de entradas al cine que se pueden comprar: ", cant)

# Llamada a la función principal
calcularEntradasCine()