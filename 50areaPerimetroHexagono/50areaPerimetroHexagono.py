def calcularAreaPerimetroHexagono():
    # Declaración de variables
    p = 0.0
    a = 0.0
    ap = 0.0
    l = 0.0

    # Área del hexágono
    print("ÁREA DEL HEXÁGONO")
    print("PERÍMETRO : ", end="")
    p = float(input())
    print("APOTEMA : ", end="")
    ap = float(input())
    a = (p * ap) / 2
    print("ÁREA : ", a, "cm2")
    print("")

    # Perímetro del hexágono
    print("PERÍMETRO DEL HEXÁGONO")
    print("LADO : ", end="")
    l = float(input())
    p = 6 * l
    print("PERÍMETRO : ", p, "cm")

# Llamada a la función principal
calcularAreaPerimetroHexagono()