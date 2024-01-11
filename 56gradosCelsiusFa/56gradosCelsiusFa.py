def convertirCelsiusAFahrenheit():
    # Declaración de variables
    c = float()
    f = float()

    # Conversión de Celsius a Fahrenheit
    print("GRADOS CELSIUS : ", end="")
    while True:
        try:
            c = float(input())
            break
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    f = (c * 9/5) + 32
    print("A FAHRENHEIT : ", f)

# Llamada a la función principal
convertirCelsiusAFahrenheit()
