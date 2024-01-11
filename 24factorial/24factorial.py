def factorial():
    fact = 1
    while True:
        try:
            num = int(input(f'Factorial a calcular: '))
            break
        except ValueError:
            print('Valor incorrecto')
    print('Serie factorial')
    
    for i in range (1, num + 1):
        print(f'{(num + 1)-i}', end=' ')
        fact = fact * i
    print(f'El factorial es {fact}')
factorial()