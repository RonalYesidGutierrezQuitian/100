def graficaAsteriscos():
    xn = 7
    for f in range(1, 8):
        serie = ""
        if f >= 5:
            xn = xn + 2
        for c in range(1, xn - f + 1):
            serie += ' * '
        print(serie)
graficaAsteriscos()
