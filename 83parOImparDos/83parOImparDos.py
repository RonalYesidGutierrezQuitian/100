def verificarParImpar():
    # Mostrar si un número es par o impar
    while True:
        try:
            num = int(input('Ingrese un número para verificar si es par o impar: '))
            if num % 2 == 0:
                print(f'{num} es PAR')
            else:
                print(f'{num} es IMPAR')
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')
verificarParImpar()