def contarLetrasFrase(refran):
    refran_sin_espacios = ""
    for letra in refran:
        if letra != " ":
            refran_sin_espacios += letra
    return refran_sin_espacios

def contarLetras(refran_sin_espacios):
    conteo = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'CONSONANTES': 0}

    for letra in refran_sin_espacios:
        letra = letra.upper()
        if letra in ['A', 'E', 'I', 'O', 'U']:
            conteo[letra] += 1
        elif letra.isalpha():
            conteo['CONSONANTES'] += 1

    return conteo

def imprimirResultados(conteo):
    total_vocales = conteo['A'] + conteo['E'] + conteo['I'] + conteo['O'] + conteo['U']
    print("CANTIDAD DE VOCALES: ", total_vocales)
    print("CANTIDAD DE CONSONANTES: ", conteo['CONSONANTES'])

def main():
    # Obtener el refrán
    print("MUESTRA LAS LETRAS")
    print("Ingrese Refran: ")
    ref = input()

    # Contar letras en el refrán
    refran_sin_espacios = contarLetrasFrase(ref)
    conteo_letras = contarLetras(refran_sin_espacios)

    # Imprimir resultados
    imprimirResultados(conteo_letras)

# Llamar a la función principal
main()
