def dibujarTriangulo():
    # Declaración de variables
    altura = 0
    caract = ""

    # Entrada de datos
    while True:
        try:
            altura = int(input("Altura del Triángulo: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    caract = input("Ingrese un carácter: ")

    # Dibujar triángulo
    for i in range(1, altura + 1):
        for j in range(1, altura - i + 1):
            print(" ", end="")
        for j in range(1, (i * 2) + 1):
            print(caract, end="")
        print(" ")

# Llamada a la función principal
dibujarTriangulo()