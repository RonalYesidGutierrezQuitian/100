def mostrarNumeroEnRomanos():
    while True:
        try:
            num = int(input("Ingrese un número del 1 al 10: "))
            if 1 <= num <= 10:
                break
            else:
                print('Número fuera de rango. Intente de nuevo.')
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    print("\nCONVERSIÓN A NÚMERO ROMANO")

    if num == 1:
        print("EN ROMANOS: I")
    elif num == 2:
        print("EN ROMANOS: II")
    elif num == 3:
        print("EN ROMANOS: III")
    elif num == 4:
        print("EN ROMANOS: IV")
    elif num == 5:
        print("EN ROMANOS: V")
    elif num == 6:
        print("EN ROMANOS: VI")
    elif num == 7:
        print("EN ROMANOS: VII")
    elif num == 8:
        print("EN ROMANOS: VIII")
    elif num == 9:
        print("EN ROMANOS: IX")
    elif num == 10:
        print("EN ROMANOS: X")

# Llamada a la función principal
mostrarNumeroEnRomanos()