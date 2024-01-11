def determinarEdad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            break
        except ValueError:
            print('Dato inválido. Ingrese un número entero válido.')

    if edad >= 18:
        print(f"La persona con {edad} años es mayor de edad.")
    else:
        print(f"La persona con {edad} años es menor de edad.")

# Llamada a la función principal
determinarEdad()