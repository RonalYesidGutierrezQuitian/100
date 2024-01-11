def calcular_area(base, altura):
    return (base * altura) / 2

def calcular_base(altura, area):
    return (area * 2) / altura

def calcular_altura(base, area):
    return (area * 2) / base

def mostrarInfoTriangulo():
    opc = int(input("MENU DE OPCIONES DE UN TRIANGULO\n"
                    "__________________________________\n"
                    "1. Área de un triángulo, dada la base y la altura\n"
                    "2. Base de un triángulo, dada la altura y el área\n"
                    "3. Altura de un triángulo, dada la base y el área\n"
                    "Selecciona una opción: "))

    if opc == 1:
        base = float(input("BASE: "))
        altura = float(input("ALTURA: "))
        area = calcular_area(base, altura)
        print("EL ÁREA ES: ", area)
    elif opc == 2:
        altura = float(input("ALTURA: "))
        area = float(input("ÁREA: "))
        base = calcular_base(altura, area)
        print("LA BASE ES: ", base)
    elif opc == 3:
        base = float(input("BASE: "))
        area = float(input("ÁREA: "))
        altura = calcular_altura(base, area)
        print("LA ALTURA ES: ", altura)
    else:
        print("ERROR. OPCIÓN INCORRECTA")


# Llamada a la función principal
mostrarInfoTriangulo()