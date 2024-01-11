def simularLogin():
    usuario = input("INGRESE USUARIO: ")
    while True:
        try:
            clave = int(input("INGRESE CLAVE: "))
            break
        except ValueError:
            print('Clave inválida. Ingrese un número.')

    if usuario == "ADMIN" and clave == 123456:
        print("ACCESO PERMITIDO")
    else:
        print("ACCESO DENEGADO")


# Llamada a la función principal
simularLogin()