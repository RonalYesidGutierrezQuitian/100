def calcularDiasTranscurridos():
    # Declaración de variables
    mes = 0
    dia = 0
    tiempo = 0

    # Entrada de datos
    while True:
        try:
            print("Nro DE MES  : ", end="")
            mes = int(input())
            print("Nro DE DIAS : ", end="")
            dia = int(input())
            break
        except ValueError:
            print('Datos inválidos. Ingrese números enteros.')

    # Proceso
    tiempo = (((mes - 1) * 30) + dia)

    # Salida
    print("\nLOS DÍAS TRANSCURRIDOS SON  : ", tiempo)

# Llamada a la función principal
calcularDiasTranscurridos()
