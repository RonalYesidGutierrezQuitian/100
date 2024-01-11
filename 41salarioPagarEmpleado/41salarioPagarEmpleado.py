def calcularSalarioConDescuento():
    # Declaración de variables
    sueldo_base = 0.0
    descuento = 0.20
    salario_final = 0.0

    # Entrada de datos
    while True:
        try:
            print("Ingrese el sueldo base del empleado: $", end="")
            sueldo_base = float(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número.')

    # Proceso
    salario_final = sueldo_base - (sueldo_base * descuento)

    # Salida
    print("\nSalario a pagar con descuento del 20%: $", salario_final)

# Llamada a la función principal
calcularSalarioConDescuento()