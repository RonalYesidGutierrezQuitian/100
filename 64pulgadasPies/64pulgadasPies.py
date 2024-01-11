def convertirPulgadasAPies():
    # Declaración de variables
    pulgadas = 0.0
    pies = 0.0

    # Entrada de datos
    print("CONVERTIR DE PULGADAS A PIES")
    while True:
        try:
            pulgadas = float(input("Ingrese pulgadas: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Conversión de pulgadas a pies
    pies = pulgadas / 12

    # Salida de resultados
    print(f"{pulgadas} pulgadas equivalen a {pies} pies.")

# Llamada a la función principal
convertirPulgadasAPies()