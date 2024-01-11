def serieFibonacci ():
    while True:
        a = 0
        b = 1
        c = 0
        while True:
                try:
                    num = int(input('Inserte un numero del que quiera ver la Serie Fibonacci\n->: '))
                    break
                except ValueError:
                    print('el dato ingresado no es un entero')
        for i in range (num):
            print(f'{c},')
            a = b
            b = c
            c = a + b
serieFibonacci ()