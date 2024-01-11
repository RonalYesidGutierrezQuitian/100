def numeroIngresadoPrimoOno():
	while True:
		try:
			num = int(input('Ingrese un número: '))
			break
		except ValueError:
			print('Dato invalido')
	divisi = 0
	for i in range(1,num+1):
		if ((num % i) == 0):
			divisi += 1
	if (divisi == 2):
		print('Numero Primo')
	else:
		print('Numero no Primo')

numeroIngresadoPrimoOno()