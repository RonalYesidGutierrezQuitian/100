def mostrarUnidadDecenaCentena():
    # Declaración de variables
    num = 0
    cen = 0
    res = 0
    dec = 0
    uni = 0

    # Entrada de datos
    while True:
        try:
            print("INGRESE Nro. DE 3 CIFRAS : ", end="")
            num = int(input())
            if 99 < num < 1000:
                break
            else:
                raise ValueError('Número no válido. Ingrese un número de 3 cifras.')
        except ValueError:
            print('Dato inválido. Ingrese un número de 3 cifras.')

    # Proceso
    cen = num // 100
    res = num % 100
    dec = res // 10
    uni = res % 10

    # Salida
    print("\nCENTENA : ", cen)
    print("DECENA  : ", dec)
    print("UNIDAD  : ", uni)

# Llamada a la función principal
mostrarUnidadDecenaCentena()