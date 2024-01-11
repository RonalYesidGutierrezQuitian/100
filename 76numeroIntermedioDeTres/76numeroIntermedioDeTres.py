def mostrarNumeroIntermedio():
    numeros = []

    # Ingreso de 3 números con validación
    for i in range(3):
        while True:
            try:
                numero = float(input(f"Ingrese el número {i + 1}: "))
                break
            except ValueError:
                print('Dato inválido. Ingrese un número válido.')

        numeros.append(numero)

    # Ordenar la lista de números
    numeros.sort()

    # Mostrar el número intermedio
    if numeros[0] == numeros[1] == numeros[2]:
        print("Los tres números son iguales.")
    else:
        print(f"El número intermedio es: {numeros[1]}")

# Llamada a la función principal
mostrarNumeroIntermedio()