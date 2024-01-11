def numerosEntreRangosAyB():
    while True:
        try:
            a = int(input('Ingrese en valor de A: '))
            b = int(input('Ingrese en valor de B: '))
            break
        except ValueError:
            print('Dato invalido')
    if (a < b):
        for i in range (a + 1, b):
            print (i)
    else:
          for i in range (b + 1, a):
            print (i)
numerosEntreRangosAyB()