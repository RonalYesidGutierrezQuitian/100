import math

def calcularAreaPerimetroCirculo():
    # Declaración de variables
    p = float()
    a = float()
    r = float()

    # Área del círculo
    print("ÁREA DEL CÍRCULO")
    while True:
        try:
            print("RADIO : ", end="")
            r = float(input())
            break
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    a = math.pi * (r**2)
    print("ÁREA : ", a)
    print("")

    # Perímetro del círculo
    print("PERÍMETRO DEL CÍRCULO")
    p = 2 * math.pi * r
    print("PERÍMETRO : ", p)

# Llamada a la función principal
calcularAreaPerimetroCirculo()