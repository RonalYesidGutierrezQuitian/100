def sumatoria():
    v = 4
    v1 = 5
    v2 = 1
    x = 2
    x1 = 0.5
    operacion = '-'
    sumatoria = 0  # Variable para almacenar el resultado de la sumatoria
    while True:
        try:
            num = int(input('Ingrese el número de iteraciones: '))
            break
        except ValueError:
            print('Valor incorrecto')

    for i in range(1, num+1):
        if (i != num):
            print(f'{v}/{x} {operacion} ', end=' ')
        else:
            print(f'{v}/{x} {operacion}...', end=' ')

        if ((i % 2) == 1):
            operacion = '+'
            sumatoria = (sumatoria + (v / x))
        else:
            operacion = '-'
            sumatoria = (sumatoria - (v / x))

        v = (v + v1)
        v1 = (v1 + v2)
        v2 = (v2 + 1)
        x = (x * x1)
        x1 = (x1 + x1)

    print(f'\nResultado: {sumatoria}')

sumatoria()