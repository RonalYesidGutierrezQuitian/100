#Pedir 10 numeros y determinar cuantos son impares y cuantos pares
def definicionParImpar():
	while True:
		pares = 0
		impares = 0
		for i in range(10):
			while True:
				try:
					numbs = int(input(f'Ingrese el numero {i+1}->: '))
					break
				except ValueError:
					print('Dato invalido, intente nuevamente')
			if ((numbs % 2) == 0):
				par =+ 1
			else:
				impar =+ 1
		print(f'cantidad de pares:{par}\ncantidad de impares:{impar}')
		ejecutar = input('Desea emepzar nuevamente S(si) cualquier otra tecla(no)->: ').lower()
		if ejecutar not in ['s','si']:
			break
definicionParImpar()