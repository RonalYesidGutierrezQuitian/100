def calcularVentasHyM():
    while True:
        try:
            empleados = int(input('Ingrese el numero de empleados: '))
            break
        except ValueError:
            print('Dato invalido')
    tv_h = 0
    tv_m = 0
    muj = 0

    for cont in range (1, empleados+1):
        print(f'Empelado #: {cont} de {empleados}')
        nomb = input('Ingrese el nombre: ')
        while True:
            try:
                genero = input('Genero H/M: ').lower()
                if genero not in ['h','m']:
                    raise ValueError ('Opcion invalida debe ser H o M')
                break
            except ValueError:
                print('Opcion invalida debe ser un string H o M')
        while True:
            try:
                ventas = int(input('Ingrese el numero de ventas del empleado: '))
                break
            except ValueError:
                print('Dato invalido de ventas')  
        if (genero == 'h'):
            tv_h += ventas
        else:
            tv_m += ventas
            muj += 1
    print(f'Total ventas hombre: {tv_h}')
    print(f'Total ventas mujeres: {tv_m}')
    print(f'\nPorcentaje mujeres: {(muj * 100)/empleados}%')
calcularVentasHyM()