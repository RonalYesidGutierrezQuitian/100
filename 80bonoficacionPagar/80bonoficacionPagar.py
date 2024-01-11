def calcularBonificacion():
    while True:
        try:
            venta = float(input("Ingrese el monto de venta: $"))
            break
        except ValueError:
            print('Dato inválido. Ingrese un monto válido.')

    print("\nCALCULANDO BONIFICACIÓN")
    if venta > 2000:
        bonificacion = venta * 0.10
        print(f"BONIFICACIÓN 10%: ${bonificacion:.2f}")
    else:
        bonificacion = venta * 0.50
        print(f"BONIFICACIÓN 50%: ${bonificacion:.2f}")

# Llamada a la función principal
calcularBonificacion()