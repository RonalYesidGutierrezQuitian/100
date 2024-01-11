def mostrarNombrePrograma():
    programas = {'V': 'Visual Basic', 'P': 'C#', 'J': 'Java', 'F': 'Fortran'}

    while True:
        try:
            print("Letra (V-P-J-F): ")
            letra = input().upper()

            if letra in programas:
                print(programas[letra])
                break
            else:
                print("Error en la letra, intente de nuevo.")
        except ValueError:
            print('Dato inválido. Intente de nuevo.')

# Llamada a la función principal
mostrarNombrePrograma()