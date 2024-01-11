def calcularSueldo():
    try:
        sueldo_base = float(input("Sueldo Base (Cop/.): "))
        categoria = int(input("Categoria (1.A - 2.B - 3.C - 4.D): "))

        if categoria == 1:
            bonificacion = sueldo_base * 0.1
        elif categoria == 2:
            bonificacion = sueldo_base * 0.2
        elif categoria == 3:
            bonificacion = sueldo_base * 0.3
        elif categoria == 4:
            bonificacion = sueldo_base * 0.5
        else:
            print("Error en la categoría.")
            return

        sueldo_neto = sueldo_base + bonificacion

        print(f"BONIFICACION : Cop/. {bonificacion}")
        print(f"SUELDO NETO  : Cop/. {sueldo_neto}")

    except ValueError:
        print('Dato inválido. Por favor, ingrese números válidos.')

# Llamada a la función principal
calcularSueldo()