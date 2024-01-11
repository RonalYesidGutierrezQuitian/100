def calcularIGV():
    # Declaración de variables
    monto = 0.0
    igv = 0.0

    # Entrada de datos
    print("01 CALCULAR EL IGV")
    print("")
    while True:
        try:
            monto = float(input("INGRESE MONTO DE DINERO : $"))
            break
        except ValueError:
            print('Dato inválido. Intente de nuevo.')

    # Cálculo del IGV
    igv = monto * 0.18

    # Salida de resultados
    print(f"EL IGV/18% ES : $ {igv:.2f}")

# Llamada a la función principal
calcularIGV()