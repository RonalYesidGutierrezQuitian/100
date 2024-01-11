def ordenarNumeros():
    while True:
        try:
            n1 = int(input("Ingrese el primer número: "))
            n2 = int(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print('Datos inválidos. Ingrese números enteros válidos.')

    print("\nNúmeros ordenados de mayor a menor:")
    if n1 > n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)

# Llamada a la función principal
ordenarNumeros()