def otroMasDeSerie():
    while True:
        try:
            n = int(input(f'Factorial a calcular: '))
            break
        except ValueError:
            print('Valor incorrecto')
    suma = 1
    d = 3
    if (n > 1):
        print(f'{suma} + ', end=' ')
        for i in range (2, n+1):
            if (i == n):
                print(f'{i}/{d}', end=' ')
            else:
                print(f"{i}/{d} + ", end=' ')
            suma = (suma + (i/d))
            d = (d + 2)
    print(f'La suma es {suma}')
otroMasDeSerie()