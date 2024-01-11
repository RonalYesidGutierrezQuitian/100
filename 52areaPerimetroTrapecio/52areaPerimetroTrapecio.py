def calcularAreaPerimetroTrapecio():
    # Declaración de variables
    p = 0.0
    a = 0.0
    b = 0.0
    bb = 0.0
    h = 0.0
    l1 = 0.0
    l2 = 0.0
    l3 = 0.0
    l4 = 0.0

    # Área del trapecio
    print("ÁREA DEL TRAPECIO")
    print("BASE MAYOR  : ", end="")
    b = float(input())
    print("BASE MENOR  : ", end="")
    bb = float(input())
    print("ALTURA      : ", end="")
    h = float(input())
    a = ((b + bb) * h) / 2
    print("ÁREA : ", a, "cm2")
    print("")

    # Perímetro del trapecio
    print("PERÍMETRO DEL TRAPECIO")
    print("LADO 01 : ", end="")
    l1 = float(input())
    print("LADO 02 : ", end="")
    l2 = float(input())
    print("LADO 03 : ", end="")
    l3 = float(input())
    print("LADO 04 : ", end="")
    l4 = float(input())
    p = l1 + l2 + l3 + l4
    print("PERÍMETRO : ", p, "cm")

# Llamada a la función principal
calcularAreaPerimetroTrapecio()