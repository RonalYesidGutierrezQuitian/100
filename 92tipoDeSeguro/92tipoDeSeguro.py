def calcularPagoSeguro():
    while True:
        try:
            print("TIPOS DE SEGURO")
            print("1. X")
            print("2. Y")
            print("3. Z")

            seguro = int(input("OPCION: "))

            if seguro == 1:
                print("Pago mensual: $45")
                break
            elif seguro == 2:
                print("Pago mensual: $30")
                break
            elif seguro == 3:
                print("Pago mensual: $15")
                break
            else:
                print("Error en el tipo de seguro")
        except ValueError:
            print('Opción inválida. Intente de nuevo.')

# Llamada a la función principal
calcularPagoSeguro()