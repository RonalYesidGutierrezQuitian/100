def obtener_numero_valido():
    while True:
        try:
            num = int(input('Ingrese un número mayor o igual a 3: '))
            if num < 3:
                raise ValueError('El número debe ser mayor o igual a 3')
            return num
        except ValueError:
            print('Dato inválido. Por favor, ingrese un número entero mayor o igual a 3.')

def dibujar_triangulo_secuencia(num):
    val = 1

    for x in range(1, num + 1):
        espacios = " " * (num - x)
        print(espacios, end="")
        
        contador = 1
        for f in range(1, val + 1):
            print(contador, end="")
            contador = 0 if contador == 9 else contador + 1
        
        val += 2
        print("")

def main():
    print("MUESTRA GRÁFICA DE NÚMEROS COMO TRIÁNGULO.")
    num = obtener_numero_valido()
    dibujar_triangulo_secuencia(num)

# Llamar a la función principal
main()