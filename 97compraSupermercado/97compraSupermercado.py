from random import randint
def calcularDescuentoCompra():
    try:
        compra = float(input("VALOR DE COMPRA: COP/. "))
        input("PULSE ENTER ... ")
        colores = {1: "BLANCO", 2: "VERDE", 3: "NEGRO", 4: "CELESTE", 5: "ROJO"}
        color = randint(1, 5)
        if color in colores:
            print(f"COLOR: {colores[color]}")
            descuento = 1.0 if color == 1 else 0.5 if color == 2 else 0.4 if color == 3 else 0.05 if color == 4 else 0
            print(f"DESCUENTO: COP/. {descuento}")
            importe_descuento = compra * descuento
            print(f"IMPORTE DESCUENTO: COP/. {importe_descuento}")
            pago_final = compra - importe_descuento
            print(f"PAGO FINAL: COP/. {pago_final}")
        else:
            print("Color no válido.")
    except ValueError:
        print('Dato inválido. Por favor, ingrese un número válido.')
# Llamada a la función principal
calcularDescuentoCompra()