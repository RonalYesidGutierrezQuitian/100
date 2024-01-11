def calcularIGV():
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: $"))
            cant = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print('Datos inválidos. Ingrese valores numéricos.')

    monto = precio * cant
    igv = 0

    print("\nCALCULANDO IGV SEGÚN EL MONTO DE COMPRA")
    print("PRECIO UNITARIO : $/.", precio)
    print("CANTIDAD        : ", cant)

    if monto > 100:
        igv = monto * 0.18

    print("\nTOTAL           : $/.", monto)
    print("IGV 18%         : $/.", igv)
    print("TOTAL A PAGAR   : $/.", monto + igv)

# Llamada a la función principal
calcularIGV()