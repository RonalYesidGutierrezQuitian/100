def numerosCapicua():
    for i in range(100, 1000):
        c = i // 100  # Obtener la centena
        r = i % 100
        c1 = r // 10  # Obtener la decena
        r1 = r % 10   # Obtener la unidad

        if i == (r1 * 100) + (c1 * 10) + c:
            print(i, end=' ')
numerosCapicua()
