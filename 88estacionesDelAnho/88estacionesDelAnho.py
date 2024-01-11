def mostrarEstacionDelAno():
    while True:
        try:
            num = int(input("Ingrese un número del 1 al 4: "))
            if 1 <= num <= 4:
                break
            else:
                print('Número fuera de rango. Intente de nuevo.')
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    print("\nESTACIÓN DEL AÑO")

    if num == 1:
        print("ES VERANO")
    elif num == 2:
        print("ES OTOÑO")
    elif num == 3:
        print("ES INVIERNO")
    elif num == 4:
        print("ES PRIMAVERA")

# Llamada a la función principal
mostrarEstacionDelAno()