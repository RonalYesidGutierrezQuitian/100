def realizarOperaciones():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    print("OPERACIONES BÁSICAS")
    print("(1) SUMA")
    print("(2) RESTA")
    print("(3) MULTIPLICACIÓN")
    print("(4) DIVISIÓN")

    while True:
        try:
            operador = int(input("Seleccione un operador (1-4): "))
            if 1 <= operador <= 4:
                break
            else:
                print('Número fuera de rango. Intente de nuevo.')
        except ValueError:
            print('Dato inválido. Ingrese un número válido.')

    if operador == 1:
        resultado = num1 + num2
        print(f"SUMA: {num1} + {num2} = {resultado}")
    elif operador == 2:
        resultado = num1 - num2
        print(f"RESTA: {num1} - {num2} = {resultado}")
    elif operador == 3:
        resultado = num1 * num2
        print(f"MULTIPLICACIÓN: {num1} x {num2} = {resultado}")
    elif operador == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"DIVISIÓN: {num1} / {num2} = {resultado}")
        else:
            print("No se puede dividir por cero. Intente con otro número.")

# Llamada a la función principal
realizarOperaciones()