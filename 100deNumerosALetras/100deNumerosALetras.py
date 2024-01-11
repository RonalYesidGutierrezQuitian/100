def convertir_numero_a_letras():
    print("PASAR DE NUMEROS A LETRAS")
    while True:
        try:
            num = int(input("INGRESE NUMERO DE HASTA 2 CIFRAS: "))
            if 0 < num < 100:
                break
            else:
                print("NUMERO INCORRECTO. Debe estar entre 1 y 99.")
        except ValueError:
            print('Dato inválido')

    colores_decenas = ["", "DIEZ", "VEINTI", "TREINTA", "CUARENTA", "CINCUENTA",
                       "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]

    colores_unidades = ["", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS",
                        "SIETE", "OCHO", "NUEVE"]

    if 10 <= num < 16:
        especiales = {10: "DIEZ", 11: "ONCE", 12: "DOCE", 13: "TRECE", 14: "CATORCE", 15: "QUINCE"}
        print(especiales[num])
    else:
        dec = num // 10
        uni = num % 10

        decena = colores_decenas[dec]
        unidad = colores_unidades[uni]

        if uni != 0 and dec != 1:
            print(decena, "Y", unidad)
        else:
            print(decena, unidad)


convertir_numero_a_letras()