def serieGraficaNumeros():
    for i in range (1, 10):
        s = 0
        serie = 0
        for j in range (1, 11-i):
            s = (10 - i)
            serie = (serie * 10) + s
        print(serie)
serieGraficaNumeros()