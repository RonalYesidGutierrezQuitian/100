def calcularRombo():
    # Declaración de variables
    p = 0.0
    a = 0.0
    d = 0.0
    dd = 0.0
    l = 0.0

    # Área del rombo
    print("ÁREA DEL ROMBO")
    print("DIÁMETRO MAYOR : ", end="")
    while True:
        try:
            d = float(input())
            break
        except ValueError:
            print('Dato inválido. Intente de nuevo.')

    print("DIÁMETRO MENOR : ", end="")
    while True:
        try:
            dd = float(input())
            break
        except ValueError:
            print('Dato inválido. Intente de nuevo.')

    a = (d * dd) / 2
    print("ÁREA : ", a, "cm²")
    print("")

    # Perímetro del rombo
    print("PERÍMETRO DEL ROMBO")
    print("LADO : ", end="")
    while True:
        try:
            l = float(input())
            break
        except ValueError:
            print('Dato inválido. Intente de nuevo.')

    p = 4 * l
    print("PERÍMETRO : ", p, "cm")

# Llamada a la función principal
calcularRombo()