def calcularAreaPerimetroTriangulo():
    # Declaración de variables
    p = 0.0
    l = 0.0
    a = 0.0
    b = 0.0
    h = 0.0

    # Área del triángulo
    print("ÁREA DEL TRIÁNGULO ")
    print("BASE   : ", end="")
    b = float(input())
    print("ALTURA : ", end="")
    h = float(input())
    a = (b * h) / 2
    print("ÁREA  : ", a, "cm.")
    print("")

    # Perímetro del triángulo equilátero
    print("PERÍMETRO DEL TRIÁNGULO EQUILÁTERO")
    print("LADO ; ", end="")
    l = float(input())
    p = l * 3
    print("PERÍMETRO  : ", p, "cm.")

# Llamada a la función principal
calcularAreaPerimetroTriangulo()