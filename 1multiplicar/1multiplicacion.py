def mostrar_tabla_multiplicar():
    while True:
        print('Vamos a ver las tablas de multiplicar')
        # Bucle hasta que se ingrese un número válido
        while True:
            try:
                num = int(input('Ingrese el número del cual quiere conocer la tabla de multiplicar: '))
                break  # Salir del bucle si la entrada es válida
            except ValueError:
                print('Dato inválido. Por favor, ingrese un número entero.')
        # Salida de datos: Mostrar la tabla de multiplicar del número ingresado
        for i in range(1, 13):
            print(f'{num} x {i} = {num * i}')
        continuarC = input('\n¿Desea continuar? S(si) cualquier otra tecla(no): ').lower()
        if continuarC not in ['s', 'si']:
            break  # Salir del bucle principal si el usuario no desea continuar
# Llamada a la función principal
mostrar_tabla_multiplicar()