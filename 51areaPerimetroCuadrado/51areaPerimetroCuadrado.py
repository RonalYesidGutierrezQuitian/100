def calcularAreaPerimetroCuadrado():
    # Declaración de variables
    p = 0.0
    a = 0.0
    l = 0.0

    # Área del cuadrado
    print("ÁREA DEL CUADRADO")
    print("LADO  : ", end="")
    l = float(input())
    a = l * l
    print("ÁREA : ", a)
    print("")

    # Perímetro del cuadrado
    print("PERÍMETRO DEL CUADRADO")
    p = 4 * l
    print("PERÍMETRO : ", p)

# Llamada a la función principal
calcularAreaPerimetroCuadrado()