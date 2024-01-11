def calcularIVA():
    # Declaración de variables
    costo = 0.0
    iva = 0.0
    totpagar = 0.0

    # Entrada de datos
    print("\nCALCULAR IVA DEL MONTO TOTAL A PAGAR")
    while True:
        try:
            costo = float(input("Costo de la Casa: $ "))
            iva = float(input("Valor de IVA (%): "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Cálculo del IVA y monto total a pagar
    totpagar = costo + (costo * (iva / 100))

    # Salida de resultados
    print(f"\nIVA de {iva}%: $ {(costo * (iva / 100))}")
    print(f"TOTAL A PAGAR: $ {totpagar}")

# Llamada a la función principal
calcularIVA()