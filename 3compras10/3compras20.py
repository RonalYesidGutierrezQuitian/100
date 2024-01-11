def compras10():
    #Inicia un bucle infinito para permitir al usuario realizar múltiples selecciones.
    while True:
        #Inicializa la variable 'total' para el cálculo del monto total de la compra.
        total = 0
        #Imprime el encabezado del menú.
        print('MENU\n')
        #Define un diccionario de productos con sus respectivos precios.
        productos = {'Cafe': 1000, 'Pan': 400, 'Huevo': 600, 'Leche': 3000}
        #Utiliza un bucle 'for' y 'enumerate' para imprimir las opciones del menú numeradas.
        for i, (producto, precio) in enumerate(productos.items(), 1):
            print(f'{i}. {producto}: ${precio}')
        #Utiliza un bucle 'for' para realizar hasta 10 selecciones de productos.
        for i in range(10):
            #Inicia un bucle 'while' para garantizar que el usuario ingrese un número válido.
            while True:
                try:
                    #Solicita al usuario seleccionar un producto mediante un número (1-6).
                    compra = int(input(f'Seleccione un producto para añadir al carrito de compras (1-{len(productos)}): '))
                    #Valida que la entrada sea un número válido dentro del rango de opciones.
                    if 1 <= compra <= len(productos):
                        break
                    else:
                        print(f'Por favor, ingrese un número válido entre 1 y {len(productos)}.')
                except ValueError:
                    #Captura y maneja la excepción si el usuario no ingresa un número válido.
                    print('Por favor, ingrese un dato válido.')
            #Obtener el nombre del producto seleccionado
            producto_seleccionado = list(productos.keys())[compra-1]
            #Obtener el precio del producto seleccionado utilizando el método get()
            precio_producto = productos.get(producto_seleccionado, 0)
            #Sumar el precio del producto al total de la compra
            total += precio_producto
            print(f'Ha seleccionado: {producto_seleccionado} : Valor {precio_producto}')
            print(f'Total actual: ${total}')
    #Fin del bucle principal. Este punto se alcanzará solo si el usuario decide salir del programa.
        break
compras10()