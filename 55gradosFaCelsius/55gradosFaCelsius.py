def convertirFahrenheitACelsius():
    # Declaración de variables
    c = float()
    f = float()

    # Conversión de Fahrenheit a Celsius
    print("GRADOS FAHRENHEIT : ", end="")
    while True:
        try:
            f = float(input())
            break
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    c = (f - 32) * (5/9)
    print("A CELSIUS : ", c)

# Llamada a la función principal
convertirFahrenheitACelsius()