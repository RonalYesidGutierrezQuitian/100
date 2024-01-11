import math

def calcularAreaYVolumenCilindro():
    # Declaración de variables
    radio = 0.0
    altura = 0.0
    area = 0.0
    volumen = 0.0

    # Entrada de datos
    print("CALCULAR ÁREA Y VOLUMEN DE UN CILINDRO")
    while True:
        try:
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            break
        except ValueError:
            print('Entrada inválida. Intente de nuevo.')

    # Cálculos
    area = 2 * math.pi * radio * (altura + radio)
    volumen = math.pi * (radio**2) * altura

    # Salida de resultados
    print("\nÁREA TOTAL DEL CILINDRO :", area, "cm2")
    print("VOLUMEN DEL CILINDRO    :", volumen, "cm3")

# Llamada a la función principal
calcularAreaYVolumenCilindro()