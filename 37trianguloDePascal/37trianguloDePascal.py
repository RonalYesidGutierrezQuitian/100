#ALGORITMO QUE MUESTRA EL TRIÁNGULO DE PASCAL
def mostrarTrianguloPascal():
    print("MOSTRAR EL TRIANGULO DE PASCAL")

    # Ingreso de datos
    while True:
        try:
            n = int(input("Ingrese DIMENSION [MENOS O IGUAL A 20]: "))
            if 1 <= n <= 20:
                break
            else:
                raise ValueError("Número fuera de rango.")
        except ValueError:
            print("Dato inválido")

    # Inicialización de la matriz
    m = [[0] * 20 for _ in range(20)]

    # Proceso: Crear el triángulo en la matriz
    for izq in range(1, n + 1):
        for der in range(2, n + 1):
            m[izq - 1][der - 1] = 0

    # Coloca el valor de 1 en los extremos
    for izq in range(1, n + 1):
        m[izq - 1][0] = 1

    for der in range(1, n + 1):
        m[der - 1][der - 1] = 1

    for izq in range(3, n + 1):
        for der in range(2, izq + 1):
            m[izq - 1][der - 1] = m[izq - 2][der - 1] + m[izq - 2][der - 2]

    # Proceso: Mostrar el triángulo
    for izq in range(1, n + 1):
        espacios = " " * (n - izq)
        print(espacios, end="")
        for der in range(1, izq + 1):
            val = m[izq - 1][der - 1]
            if val != 0:
                print(val, end=" ")
        print("")

mostrarTrianguloPascal()
