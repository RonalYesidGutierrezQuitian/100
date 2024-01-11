def dibujarRombo():
    # Declaración de variables
    altura = 0

    # Entrada de datos y validación
    while True:
        try:
            altura = int(input("Altura del rombo (número impar): "))
            if altura % 2 == 1:
                break
            else:
                print("La altura debe ser un número impar. Intente de nuevo.")
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Dibujar rombo
    for i in range(1, altura + 1, 2):
        print(" " * ((altura - i) // 2) + "* " * ((i // 2) + 1))

    for i in range(altura - 2, 0, -2):
        print(" " * ((altura - i) // 2) + "* " * ((i // 2) + 1))

# Llamada a la función principal
dibujarRombo()