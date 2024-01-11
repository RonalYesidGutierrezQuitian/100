def obtener_numero_input(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            break
        except ValueError:
            print('Dato invalido. Por favor, ingrese un número entero válido.')
    return num
def obtener_genero_input():
    while True:
        try:
            genero = input('GÉNERO (H/M): ').upper()
            if genero not in ['H', 'M']:
                raise ValueError('Opción invalida. Debe ser H o M.')
            break
        except ValueError:
            print('Opción invalida. Debe ser H o M.')
    return genero
def calcular_edad(anio_nacimiento, mes_nacimiento, dia_nacimiento, dia_actual, mes_actual, anio_actual):
    edad = anio_actual - anio_nacimiento
    if mes_nacimiento > mes_actual or (mes_nacimiento == mes_actual and dia_nacimiento > dia_actual):
        edad -= 1
    return edad
def determinar_regalo(edad, genero):
    if edad >= 8:
        return "RECIBE TABLET"
    elif edad == 6:
        return "RECIBE CARRITO" if genero == "H" else "RECIBE MUÑECA"
    else:
        return ""
def main():
    dia_actual = 21
    mes_actual = 10
    anio_actual = 2022
    for _ in range(1, 11):
        print("DNI:", end=" ")
        dni = input()
        dia = obtener_numero_input("DÍA DE NACIMIENTO: ")
        mes = obtener_numero_input("MES DE NACIMIENTO: ")
        anio = obtener_numero_input("AÑO DE NACIMIENTO: ")

        genero = obtener_genero_input()

        print(f"FECHA ACTUAL: {dia_actual}/{mes_actual}/{anio_actual}")
        edad = calcular_edad(anio, mes, dia, dia_actual, mes_actual, anio_actual)
        print(f"EDAD: {edad} años")

        regalo = determinar_regalo(edad, genero)
        if regalo:
            print(regalo)

        print()
if __name__ == "__main__":
    main()