def contar_letras(refran):
    c = s = d = l = r = m = consonantes = 0
    for letra in refran:
        letra = letra.upper()
        if letra == "C":
            c += 1
        elif letra == "S":
            s += 1
        elif letra == "D":
            d += 1
        elif letra == "L":
            l += 1
        elif letra == "R":
            r += 1
        elif letra == "M":
            m += 1
        if letra not in ["A", "E", "I", "O", "U"]:
            consonantes += 1
    return c, s, d, l, r, m, consonantes

def main():
    refran = input("Ingrese Refran: ").replace(" ", "")
    c, s, d, l, r, m, consonantes = contar_letras(refran)
    print("CANTIDA DE C :", c)
    print("CANTIDA DE S :", s)
    print("CANTIDA DE D :", d)
    print("CANTIDA DE L :", l)
    print("CANTIDA DE R :", r)
    print("CANTIDA DE M :", m)
    print("CANTIDA DE CONSONANTES :", consonantes)
if __name__ == "__main__":
    main()