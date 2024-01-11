def calcularIGV():
    while True:
        try:
            monto = float(input("Ingrese el monto a pagar: $"))
            break
        except ValueError:
            print('Dato inválido. Ingrese un valor numérico.')

    print("\nCALCULANDO IGV 18% SI MONTO ES MAYOR A $500")
    print("MONTO A PAGAR: $", monto)

    if monto > 500:
        igv = monto * 0.18
        print("EL 18% ES: $", igv)

# Llamada a la función principal
calcularIGV()