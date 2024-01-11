def mostrarAnhosMesesDias():
    # Declaración de variables
    dias = 0
    a = 0
    m = 0
    d = 0

    # Entrada de la cantidad de días
    print("INGRESE LA CANTIDAD DE DIAS : ", end="")
    while True:
        try:
            dias = int(input())
            if dias >= 0:
                break
            else:
                print("Ingrese un valor no negativo.")
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    # Cálculos para años, meses y días
    a = dias // 365
    residuo_dias = dias % 365
    m = residuo_dias // 30
    d = residuo_dias % 30

    # Corregir el cálculo de meses y días
    if m == 12:
        a += 1
        m = 0

    # Salida de resultados
    print("Año : ", a)
    print("Mes : ", m)
    print("Día : ", d)

# Llamada a la función principal
mostrarAnhosMesesDias()