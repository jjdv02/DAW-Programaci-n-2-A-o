# Ejercicio 1
Menu =""" 
	=============================================================
		A) Añadir Cliente.
		B) Mostrar los % de los clientes premium y normales.
		G) Salir
	=============================================================
 """
print(Menu)
opcion = str(input("Introduzca una opción: "))
totalClientes = 0 
totalClientesNP = 0
totalClientesP = 0
while not (opcion == "A" or opcion == "B" or opcion == "G"):
	print("La opción introducida no es válida")
	print(Menu)
	opcion = str(input("Introduzca una opción: "))

if opcion == "A":
	premium = str(input("Indique si el cliente es premium: "))
	correoElectrónico = str(input("Introduce el correo electrónico del cliente: "))
	
	if premium == "S":
		totalClientesP += 1
		totalClientes += 1 

	elif premium == "N":
		totalClientesNP += 1
		totalClientes += 1 

	while opcion == "A":
		opcion = str(input("Introduzca una opción: "))
		premium = str(input("Indique si el cliente es premium: "))
		correoElectrónico = str(input("Introduce el correo electrónico del cliente: "))


if opcion == "B":
	# premium = int(input("Mostrar los % de los clientes premium y normales."))
	print(f"El número total de clientes es {totalClientes} ")
	print(f"El total de clientes premium es: ",{totalClientesP} / {totalClientes} * 100)
	print(f"El total de clientes normales es: ",{totalClientesNP} / {totalClientes} * 100)

if opcion == "G":
	print("Ha salido del programa")



