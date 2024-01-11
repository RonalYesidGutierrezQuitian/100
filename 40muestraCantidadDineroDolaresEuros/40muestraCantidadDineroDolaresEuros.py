def mostrarCambioDinero():
    # Declaracion de variables
    monto = 0.0
    dolar = 0.0
    euro = 0.0
    # ENTRADA
    while True:
        try:
            print("INGRESE DINERO : ", end="")
            monto = float(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número.')
    # PROCESO
    dolar = monto / 2.7
    euro = monto / 4
    # SALIDA
    print("CAMBIO A DOLAR : {:.2f}".format(dolar))
    print("CAMBIO A EURO  : {:.2f}".format(euro))
mostrarCambioDinero()
