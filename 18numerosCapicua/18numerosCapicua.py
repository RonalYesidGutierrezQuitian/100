#algoritmo que muestra si un numero es capicúa o no en python
def numerosCapicua():
    while True:
        try:
            num = int(input('Ingrese un numero: '))
            break
        except ValueError:
            print('Valor incorrecto')
    # Convertir el número a una cadena para invertirlo más fácilmente
    num_str = str(num)
    # Invertir la cadena
    num_invertido = num_str[::-1]
    print(f'Número ingresado: {num}')
    print(f'Número invertido: {num_invertido}')
    if num_str == num_invertido:
        print('Es capicúa')
    else:
        print('No es capicúa')
numerosCapicua()
