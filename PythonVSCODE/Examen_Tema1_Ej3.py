nuevoIncidente = input("¿Desea incluir un nuevo incidente?: ").upper()
totalAlumnos = int(input("Indique el número total de alumnos en el centro: "))
tipoIncidente = input("Indique el tipo de incidente (L/M/G): ").upper()
nivelIncidente = input("Indique donde ha ocurrido el incidente ESO (E) o Post-Obligatoria (P): ").upper()

contadorIncidentes = 0
contadorLeve = 0
contadorModerado = 0
contadorGrave = 0
contadorESO = 0
contadorPostobligatoria = 0

if tipoIncidente == "L":
		contadorLeve += 1
		contadorIncidentes += 1
elif tipoIncidente == "M":
		contadorModerado += 1
		contadorIncidentes += 1
elif tipoIncidente == "G":
		contadorGrave += 1
		contadorIncidentes += 1

if nivelIncidente == "E":
	contadorESO += 1
elif nivelIncidente == "P":
	contadorPostobligatoria += 1


while nuevoIncidente == "S":
	nuevoIncidente = input("¿Desea incluir un nuevo incidente?: ").upper()
	tipoIncidente = input("Indique el tipo de incidente (L/M/G): ").upper()
	nivelIncidente = input("Indique donde ha ocurrido el incidente ESO (E) o Post-Obligatoria (P): ").upper()


while nuevoIncidente == "N":
	print(f"Se han producido {contadorIncidentes} en el centro {contadorLeve} de ellos Leves, {contadorModerado} de ellos Moderados, {contadorGrave} de ellos Graves, siendo el {contadorESO / totalAlumnos * 100} % en la ESO y el {contadorPostobligatoria / totalAlumnos * 100} en Post-Obligatoria")