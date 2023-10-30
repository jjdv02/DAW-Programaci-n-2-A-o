 #Ejercicio 1:

jugador1 = str(input("Jugador1 indique su elección: "))
jugador2 = str(input("Jugador2 indique su elección: "))

if jugador1 == "papel":
	
	if jugador2 == "papel":
		print("empate")

	if jugador2 == "piedra":
		print("papel gana contra piedra")

	if jugador2 == "tijeras":
		print("papel pierde contra tijeras")

	if jugador2 == "lagarto":
		print("papel pierde contra lagarto")
	
	if jugador2 == "spock":
		print("papel gana ante spock")

	else:
		print("El/Los términos introducidos no son válidos")

elif jugador1 == "piedra":

	if jugador2 == "papel":
		print("piedra pierde contra papel")

	if jugador2 == "piedra":
		print("empate")

	if jugador2 == "tijeras":
		print("piedra gana contra tijeras")

	if jugador2 == "lagarto":
		print("piedra gana contra lagarto")
	
	if jugador2 == "spock":
		print("piedra pierde contra spock")

	else:
		print("El/Los términos introducidos no son válidos")

elif jugador1 == "tijeras":

	if jugador2 == "papel":
		print("tijeras gana contra papel")

	if jugador2 == "piedra":
		print("tijeras pierde contra piedra")

	if jugador2 == "tijeras":
		print("empate")

	if jugador2 == "lagarto":
		print("tijeras gana contra lagarto")
	
	if jugador2 == "spock":
		print("tijeras pierde contra spock")

	else:
		print("El/Los términos introducidos no son válidos")

elif jugador1 == "lagarto":

	if jugador2 == "papel":
		print("lagarto gana contra papel")

	if jugador2 == "piedra":
		print("lagarto pierde contra piedra")

	if jugador2 == "tijeras":
		print("lagarto pierde contra tijeras")

	if jugador2 == "lagarto":
		print("empate")
	
	if jugador2 == "spock":
		print("lagarto gana cont5ra spock")

	else:
		print("El/Los términos introducidos no son válidos")

elif jugador1 == "spock":

	if jugador2 == "papel":
		print("spock pierde ante papel")

	if jugador2 == "piedra":
		print("spock gana contra piedra")

	if jugador2 == "tijeras":
		print("spock gana contra tijeras")

	if jugador2 == "lagarto":
		print("spock pierde contra lagarto")
	
	if jugador2 == "spock":
		print("empate")

	else:
		print("El/Los términos introducidos no son válidos") 

		





""" # Ejercicio 3:

tamañoEmpresa = int(input("Introduzca el tamaño de su empresa: "))
edadEmpleado = int(input("Indique su edad: "))
sexoEmpleado = int(input("Indique su sexo: "))
lenguajeHabitual = str(input("Introduzca su lenguaje de programación habitual: ")) """