def mostrarNombreDelMes():
    while True:
        try:
            num = int(input("Ingrese un número del 1 al 12: "))
            if 1 <= num <= 12:
                break
            else:
                print('Número fuera de rango. Intente de nuevo.')
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    print("\nMES DEL AÑO")

    if num == 1:
        print("MES DE ENERO")
    elif num == 2:
        print("MES DE FEBRERO")
    elif num == 3:
        print("MES DE MARZO")
    elif num == 4:
        print("MES DE ABRIL")
    elif num == 5:
        print("MES DE MAYO")
    elif num == 6:
        print("MES DE JUNIO")
    elif num == 7:
        print("MES DE JULIO")
    elif num == 8:
        print("MES DE AGOSTO")
    elif num == 9:
        print("MES DE SEPTIEMBRE")
    elif num == 10:
        print("MES DE OCTUBRE")
    elif num == 11:
        print("MES DE NOVIEMBRE")
    elif num == 12:
        print("MES DE DICIEMBRE")

# Llamada a la función principal
mostrarNombreDelMes()