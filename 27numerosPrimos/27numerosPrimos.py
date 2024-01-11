def numerosPrimos():
    while True:
        try:
            num = int(input(f'De que numero quiere ver los primos: '))
            break
        except ValueError:
            print('Valor incorrecto')
    for i in range (2,num):
        divisible = 0
        for j in range (1, i + 1):
            if ((i % j) == 0):
                divisible += 1
        if (divisible == 2):
            print(f'{i}', end=' ')
        divisible = 0
numerosPrimos()