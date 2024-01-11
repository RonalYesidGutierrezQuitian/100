def mostrarColorMasVotado():
    n = 0
    r = 0
    v = 0
    a = 0
    mcolor = ""

    print("CANTIDAD DE PERSONAS : ", end="")
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print('Dato inválido')

    colores = ['ROJO', 'VERDE', 'AZUL']

    for i in range(1, n + 1):
        print(f"PERSONA Nro. {i} ", end="")
        c = ""
        while True:
            try:
                print("Seleccione un color:")
                for idx, color in enumerate(colores, 1):
                    print(f"{idx}. {color}")
                opcion = int(input())
                if 1 <= opcion <= len(colores):
                    c = colores[opcion - 1]
                    break
                else:
                    raise ValueError('Opción fuera de rango')
            except ValueError:
                print('Opción inválida. Intente de nuevo.')

        if c == "ROJO":
            r += 1
        elif c == "VERDE":
            v += 1
        else:
            a += 1

    print("\nCANTIDAD DE COLOR ROJO   : ", r)
    print("CANTIDAD DE COLOR VERDE  : ", v)
    print("CANTIDAD DE COLOR AZUL   : ", a)

    if r == v == a:
        mcolor = "TODOS LOS COLORES TIENEN LA MISMA CANTIDAD DE VOTOS"
    elif r == v and r > a and v > a:
        mcolor = "ROJO Y VERDE SON  MAS ESCOGIDOS"
    elif a == r and a > v and r > v:
        mcolor = "AZUL Y ROJO SON MAS ESCOGIDOS"
    elif a == v and a > r and v > r:
        mcolor = "VERDE Y AZUL SON MAS ESCOGIDOS"
    elif r > v and r > a:
        mcolor = "ROJO"
    elif v > r and v > a:
        mcolor = "VERDE"

    print("EL COLOR MAS ESCOGIDO ES : ", mcolor)

mostrarColorMasVotado()