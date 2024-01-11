def mostrarDiaSemana():
    while True:
        try:
            dia = int(input("Ingrese un número del 1 al 7: "))
            if 1 <= dia <= 7:
                break
            else:
                print('Número fuera de rango. Intente de nuevo.')
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    print("\nDETERMINANDO EL DÍA DE LA SEMANA")

    if dia == 1:
        print("LUNES")
    elif dia == 2:
        print("MARTES")
    elif dia == 3:
        print("MIÉRCOLES")
    elif dia == 4:
        print("JUEVES")
    elif dia == 5:
        print("VIERNES")
    elif dia == 6:
        print("SÁBADO")
    elif dia == 7:
        print("DOMINGO")

# Llamada a la función principal
mostrarDiaSemana()