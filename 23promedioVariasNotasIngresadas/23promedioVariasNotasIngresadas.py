def promedioVariasNotasIngresadas():
    while True:
        try:
            n = int(input('Ingrese la cantidad de notas: '))
            break
        except ValueError:
            print('Número inválido')
    suma = 0
    for i in range(1, n+1):
        while True:
            try:
                nota = int(input(f'Nota {i}: '))
                break
            except ValueError:
                print('Número inválido')
        suma += nota  # Acumular las notas en la suma
    print(f'Promedio: {suma / n}')
promedioVariasNotasIngresadas()
