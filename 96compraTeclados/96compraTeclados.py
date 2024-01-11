def calcularCostoTeclados():
    try:
        cantidad = int(input("Cantidad a comprar: "))

        if 1 <= cantidad <= 3:
            costo = 15
        elif 4 <= cantidad <= 8:
            costo = 11
        else:
            costo = 10

        total_pagar = costo * cantidad
        print(f"Costo por teclado: S/. {costo}")
        print(f"Total a Pagar: S/. {total_pagar}")

    except ValueError:
        print('Dato inválido. Por favor, ingrese un número válido.')

# Llamada a la función principal
calcularCostoTeclados()