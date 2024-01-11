def calcularCostoLlamada():
    tarifas = {
        1: 0.13,
        2: 0.11,
        5: 0.52,
        6: 0.99,
        8: 0.17,
        9: 0.17,
        10: 0.20,
        15: 0.59,
        20: 0.28
    }

    while True:
        try:
            print("CLAVES DE DESTINO")
            print("(1) ESTADOS UNIDOS - $0.13")
            print("(2) CANADÁ - $0.11")
            print("(5) AMÉRICA DEL SUR - $0.52")
            print("(6) AMÉRICA CENTRAL - $0.99")
            print("(8) MÉXICO - $0.17")
            print("(9) EUROPA - $0.17")
            print("(10) ASIA - $0.20")
            print("(15) ÁFRICA - $0.59")
            print("(20) OCEANÍA - $0.28")

            clave = int(input("INGRESE CLAVE DESTINO: "))
            minutos = int(input("DURACIÓN DE LA LLAMADA (en minutos): "))

            if clave in tarifas:
                costo = minutos * tarifas[clave]
                print(f"COSTO: ${costo:.2f}")
                break
            else:
                print("ERROR EN CLAVE")
        except ValueError:
            print('Datos inválidos. Ingrese números válidos.')

# Llamada a la función principal
calcularCostoLlamada()