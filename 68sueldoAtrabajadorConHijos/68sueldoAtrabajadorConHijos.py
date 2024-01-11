def calcularSalario():
    sueldobase = 0
    num_hijos = 0
    dias_no_laborales = 0
    sueldo_final = 0

    # Ingreso de datos
    print("CALCULAR EL SUELDO FINAL DE UN EMPLEADO")
    print("")
    while True:
        try:
            sueldobase = float(input("Ingrese sueldo Base: $"))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    while True:
        try:
            num_hijos = int(input("Ingrese Numero de Hijos: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    while True:
        try:
            dias_no_laborales = int(input("Ingrese Dias no Laborales Trabajados: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Cálculo del sueldo final
    sueldo_final = sueldobase + (num_hijos * 100) + (dias_no_laborales * 25)

    # Salida
    print("")
    print("SUELDO FINAL: $", sueldo_final)

# Llamada a la función principal
calcularSalario()