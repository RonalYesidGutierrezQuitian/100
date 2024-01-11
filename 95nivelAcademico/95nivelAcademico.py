def obtenerNivelAcademico():
    try:
        n1 = int(input("Ingrese Nota 1 rango (0-20): "))
        n2 = int(input("Ingrese Nota 2 rango (0-20): "))
        n3 = int(input("Ingrese Nota 3 rango (0-20): "))
        promedio = round((n1 + n2 + n3) / 3)

        if 0 <= promedio <= 10:
            print("NIVEL MALO")
        elif 11 <= promedio <= 13:
            print("NIVEL REGULAR")
        elif 14 <= promedio <= 16:
            print("NIVEL BUENO")
        elif 17 <= promedio <= 20:
            print("NIVEL MUY BUENO")
        else:
            print("Nota fuera de rango (0-20).")

    except ValueError:
        print('Dato inválido. Por favor, ingrese números válidos.')

# Llamada a la función principal
obtenerNivelAcademico()