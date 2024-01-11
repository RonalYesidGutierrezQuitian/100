def calcularCostoLlamada():
    while True:
        try:
            llamada = int(input("CANTIDAD DE MINUTOS: "))
            break
        except ValueError:
            print('Dato inválido. Ingrese un número entero.')

    costo = 0.9 * llamada if llamada <= 5 else (5 * 0.9) + (llamada - 5) * 1.1
    print(f"EL COSTO ES : $ {costo:.2f}")


# Llamada a la función principal
calcularCostoLlamada()