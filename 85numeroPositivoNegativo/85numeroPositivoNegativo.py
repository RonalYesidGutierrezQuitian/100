def verificarPositivoNegativo():
    while True:
        try:
            num = int(input("Ingrese un número: "))
            break
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    print("\nVERIFICANDO SI EL NÚMERO ES POSITIVO O NEGATIVO")

    if num >= 0:
        print("Número positivo")
    else:
        print("Número negativo")

# Llamada a la función principal
verificarPositivoNegativo()