def mostrarPorcentajeAprobadosDesaprobados():
    apro = 0
    desa = 0

    # Ingreso de Datos
    print("MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS")
    print("")
    
    while True:
        try:
            apro = float(input("INGRESE CANTIDAD DE ALUMNOS APROBADOS: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    while True:
        try:
            desa = float(input("INGRESE CANTIDAD DE ALUMNOS DESAPROBADOS: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Proceso
    total_alumnos = apro + desa
    porcentaje_aprobados = (apro / total_alumnos) * 100
    porcentaje_desaprobados = (desa / total_alumnos) * 100

    # Salida
    print("\nAPROBADOS: ", round(porcentaje_aprobados, 2), "%")
    print("DESAPROBADOS: ", round(porcentaje_desaprobados, 2), "%")

# Llamada a la función principal
mostrarPorcentajeAprobadosDesaprobados()