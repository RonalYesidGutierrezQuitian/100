def calcularAreaPerimetroRectangulo():
    # Declaración de variables
    p = 0.0
    a = 0.0
    b = 0.0
    h = 0.0

    # Área del rectángulo
    print("ÁREA DEL RECTÁNGULO")
    while True:
        try:
            print("BASE   : ", end="")
            b = float(input())
            break
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    while True:
        try:
            print("ALTURA : ", end="")
            h = float(input())
            break
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    a = b * h
    print("ÁREA : ", a, "cm")
    print("")

    # Perímetro del rectángulo
    print("PERÍMETRO DEL RECTÁNGULO")
    while True:
        try:
            p = (2 * h) + (2 * b)
            break
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    print("PERÍMETRO : ", p, "cm")

# Llamada a la función principal
calcularAreaPerimetroRectangulo()