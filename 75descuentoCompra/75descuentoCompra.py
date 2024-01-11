def calcularDescuento(monto):
    if monto >= 350:
        descuento = monto * 0.35
        print(f"DESCUENTO DEL 35%: $/. {descuento}")
    else:
        descuento = monto * 0.10
        print(f"DESCUENTO DEL 10%: $/. {descuento}")

    monto_pagar = monto - descuento
    print(f"MONTO A PAGAR: $/. {monto_pagar}")

# Entrada de datos con validación
while True:
    try:
        monto_compra = float(input("MONTO DE COMPRA: $/. "))
        break
    except ValueError:
        print('Dato inválido. Ingrese un número.')

# Llamada a la función principal
calcularDescuento(monto_compra)