def serieGraficaNumeros2():
    for i in range (1, 10):
        serie = 0
        for j in range (1, 11-i):
            serie = (serie * 10) + j
        print(serie)
serieGraficaNumeros2()