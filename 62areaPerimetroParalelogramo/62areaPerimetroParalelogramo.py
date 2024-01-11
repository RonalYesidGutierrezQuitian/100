def calcularParalelogramo():
    # Declaración de variables
    a = 0.0
    b = 0.0
    h = 0.0
    p = 0.0

    # Entrada de datos
    print("ÁREA Y PERÍMETRO DE UN PARALELOGRAMO")
    while True:
        try:
            b = float(input("BASE: "))
            h = float(input("ALTURA: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Cálculo del área y perímetro
    a = b * h
    p = 2 * (h + b)

    # Salida de resultados
    print(f"\nÁREA: {a} cm²")
    print(f"PERÍMETRO: {p} cm")

# Llamada a la función principal
calcularParalelogramo()
