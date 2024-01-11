def verificarMundial():
    while True:
        try:
            respuesta = input("¿Chile jugó el Mundial de Rusia 2018? (Verdadero/Falso): ").capitalize()
            if respuesta == 'Verdadero' or respuesta == 'Falso':
                break
            else:
                raise ValueError('Respuesta no válida. Ingrese Verdadero o Falso.')
        except ValueError as e:
            print(e)

    print("\nVERIFICANDO SI CHILE FUE AL MUNDIAL DE RUSIA 2018")

    if respuesta == 'Verdadero':
        print("Está equivocado, no fue al Mundial.")
    else:
        print("Está en lo correcto.")

# Llamada a la función principal
verificarMundial()