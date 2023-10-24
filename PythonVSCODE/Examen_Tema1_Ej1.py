# Ejercicio 1
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce un número: "))
numero3 = int(input("Introduce un número: "))
numeroPrimero = 0
numeroSegundo = 0
numeroTercero = 0

""" while numero1 <= 0 and numero2 <= 0 and numero3 <= 0"""

if numero1 < numero2 and numero1 < numero3 and numero3 > numero1:
	numeroPrimero = numero2
	numeroSegundo = numero3
	numeroTercero = numero1

elif numero1 < numero2 and numero1 < numero3 and numero3 > numero2:
	numeroPrimero = numero1
	numeroSegundo = numero3
	numeroTercero = numero2

elif numero1 < numero3:
	numeroPrimero = numero3
	numeroSegundo = numero1

elif numero1 > numero3:
	numeroPrimero = numero1
	numeroSegundo = numero3

elif numero2 < numero3:
	numeroPrimero = numero3
	numeroSegundo = numero1

elif numero2 > numero3:
	numeroPrimero = numero1
	numeroSegundo = numero3

for i in range (numeroPrimero, numeroSegundo, numeroTercero):
	print(i)

