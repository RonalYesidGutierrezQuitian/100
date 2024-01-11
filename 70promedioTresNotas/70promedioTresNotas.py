def calcularPromedio():
    nota1 = 0
    nota2 = 0
    nota3 = 0

    # Entrada de notas
    while True:
        try:
            nota1 = int(input("INGRESE NOTA 01: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    while True:
        try:
            nota2 = int(input("INGRESE NOTA 02: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    while True:
        try:
            nota3 = int(input("INGRESE NOTA 03: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Proceso
    promedio = (nota1 + nota2 + nota3) / 3

    # Salida
    print("\nEL PROMEDIO ES:", promedio)

    # Verificación de aprobación
    if promedio >= 60:
        print("APROBADO")
    else:
        print("DESAPROBADO")

# Llamada a la función principal
calcularPromedio()