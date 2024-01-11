def numeroParOimpar():
    while True:
        try:
            num = int(input('Ingrese un numero: '))
            break
        except ValueError:
            print('Dato ingresado invalido')
    sumaP = 0
    sumaI = 0
    for i in range (1, num+1):
        if ((i % 2) == 0):
            sumaP = sumaP + i
        elif ((i % 2) == 1):
            sumaI = sumaI + i
    print(f'Suma de pares: {sumaP}')
    print(f'Suma de impares: {sumaI}')
numeroParOimpar()
