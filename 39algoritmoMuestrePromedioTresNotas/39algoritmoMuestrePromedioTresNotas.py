def mostrarPromedioNotas():
    n1 = 0
    n2 = 0
    n3 = 0
    prom = 0.0

    print("Algoritmo que muestra el Promedio de Tres Notas (calificable de 0 a 100)")

    while True:
        try:
            print("INGRESE NOTA 01 : ", end="")
            n1 = int(input())
            print("INGRESE NOTA 02 : ", end="")
            n2 = int(input())
            print("INGRESE NOTA 03 : ", end="")
            n3 = int(input())
            break
        except ValueError:
            print('Dato inválido. Ingrese un número.')

    prom = (n1 + n2 + n3) / 3

    if prom >= 60:
        print("APROBADO CON {:.2f}".format(prom))
    else:
        print("DESAPROBADO CON {:.2f}".format(prom))

mostrarPromedioNotas()