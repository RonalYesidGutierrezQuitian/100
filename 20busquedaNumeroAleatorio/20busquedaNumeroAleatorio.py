import random
def busquedaNumeroAleatorio():
    sw = 0
    numA = random.randint(1,20)
    for i in range (1,4):
        while True:
            try:
                num = int(input('Igrese el numero:\n-> '))
                break
            except ValueError:
                print('Valor invalido')
        if (num == numA):
            print('Numero encontrado')
            sw = 1
            i = 3
            break
        elif (num > numA):
            if i < 3:
                print('Ingrese un numero menor')
        else:
            if i < 3:
                print('Ingrese un numero mayor')
    if (sw == 0):
        print(f'El numero a encontrar era: {numA}')
busquedaNumeroAleatorio()