def mejorAlumno ():
    while True:
        mayorPromedio = float(0.0)
        mayorPNombre = ''
        for i in range (5):
            nombre = input(f'Nombre alumno {i+1}\n->: ')
            while True:
                try:
                    promedio  = float(input(f'Ingrese en promedio de {nombre}\n->: '))
                    break
                except ValueError:
                    print('El dato ingresado no corresponde a un promedio')
            if mayorPromedio < promedio:
                mayorPromedio = promedio
                mayorPNombre = nombre
        print(f'El alumno con mayo promedio es: {mayorPNombre}: Promedio {mayorPromedio}')
        break
mejorAlumno ()