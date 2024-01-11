def productoVariosNumeros():
    pro = 1
    while True:
        try:
            n = int(input('Valor de n : '))
            break
        except ValueError:
            print('Dato ingresado invalido')
    for i in range (1, n+1):
        print(f"{i}")
        pro = (pro * i)
    print("")
    print(f'Producto de {n} es: {pro}')
productoVariosNumeros()