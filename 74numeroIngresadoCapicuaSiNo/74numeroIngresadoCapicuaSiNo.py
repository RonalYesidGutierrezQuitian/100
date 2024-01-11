def esCapicua(numero):
    num_str = str(numero)
    num_invertido = num_str[::-1]
    
    print("\nNUMERO INGRESADO :", num_str)
    print("NUMERO CAMBIADO  :", num_invertido)
    
    if num_str == num_invertido:
        print("SI ES UN NÚMERO CAPICÚA")
    else:
        print("NO ES UN NÚMERO CAPICÚA")

# Entrada de datos con validación
while True:
    try:
        num = int(input("INGRESE UN NÚMERO: "))
        break
    except ValueError:
        print('Dato inválido. Ingrese un número entero.')

# Llamada a la función principal
esCapicua(num)