def distribuirPresupuesto():
    # Declaración de variables
    presupuesto = 0.0
    gine = 0.0
    trau = 0.0
    pedi = 0.0

    # Entrada del presupuesto anual
    print("INGRESE PRESUPUESTO : ", end="")
    while True:
        try:
            presupuesto = float(input())
            if presupuesto >= 0:
                break
            else:
                print("Ingrese un valor no negativo.")
        except ValueError:
            print('Entrada no válida. Intente de nuevo.')

    # Cálculos para distribuir el presupuesto
    gine = presupuesto * 0.40
    trau = presupuesto * 0.30
    pedi = presupuesto * 0.30

    # Salida de resultados
    print("GINECOLOGIA   : $", gine)
    print("TRAUMATOLOGIA : $", trau)
    print("PEDIATRIA     : $", pedi)

# Llamada a la función principal
distribuirPresupuesto()
