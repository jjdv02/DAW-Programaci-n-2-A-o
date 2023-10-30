# 1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
""" cateto_A = int(input("Indica la medida del cateto A: "))
cateto_B = int(input("Indica la medida del cateto B: "))
cateto_C = ((cateto_A **2 + cateto_B **2) **0.5)
print(cateto_C) """

# 2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
# Para convertir Fahrenheit a grados centígrados: restar 32 y luego multiplicar por 5/ 9 o 0,555. 
# Para convertir grados centígrados a Fahrenheit: multiplicar por 9/ 5 o por 1,8 y luego sumar 32. 

""" gradoFahrenheit = int(input("Introduce un valor en grados Fahrenheit: "))
print((gradoFahrenheit - 32) * 0.555) """

# 3. Calcular la media de tres números pedidos por teclado

""" numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

print((numero1 + numero2 + numero3) / 3) """

# 4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
# cuanto deberá pagar finalmente por su compra.

"""PrecioTotal = float(input("¿Cuanto es el total de su compra?: "))
print(PrecioTotal - (PrecioTotal * 0.15))  """

# 5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
# diferencia, de modo que el resultado sea siempre positivo).

""" Numero1 = int(input("Introduce un número: "))
Numero2 = int(input("Introduce el segundo número: "))
Distancia = Numero1 - Numero2
print(Distancia)
if Distancia < 0:
	print("ERROR") """

# 6. Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano.
# Calcula y muestra la distancia entre ellos.

""" X1 = float(input("Introduce el valor de X1: "))
Y1 = float(input("Introduce el valor de Y1: "))
X2 = float(input("Introduce el valor de X2: "))
Y2 = float(input("Introduce el valor de Y2: "))

print(((X2-X1)**2 + (Y2-Y1)**2)**1/2)
 """
# 7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
# Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
# puede calcular?

""" número = float(input("Introduce un número: ")) 
raíz_cuadrada = número **1/2
raíz_cúbica = número **1/3

print("La raíz cuadrada es: ", raíz_cuadrada,)
print("La raíz cúbica es: ", raíz_cúbica) """

# 8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
# pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

""" moneda2e = float(input("Indica cuantas monedas de 2 euros tienes: "))
moneda1e = float(input("Indica cuantas monedas de 1 euro tienes: "))
moneda50cent = float(input("Indica cuantas monedas de 50 céntimos tienes: "))
moneda20cent = float(input("Indica cuantas monedas de 20 céntimos tienes: "))
moneda10cent = float(input("Indica cuantas monedas de 10 céntimos tienes: "))
print((moneda2e*2) + (moneda1e*1) + (moneda50cent*0.50) + (moneda20cent*0.20) + (moneda10cent*0.10)) """

# 9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
# exponente. Pueden ocurrir tres cosas:
# ◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
# ◦ El exponente sea 0, el resultado es 1.
# ◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

""" base = int(input("Introduce la base: "))
exponente = int(input("introduce el exponente: "))
potencia = base **exponente
print(potencia) """

# 2 elevado a 3 es 8
# 2 elevado a -3 es igual a 1 dividido entre 2*2*2 
# un número elevado a 0 es 1


# 10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
# lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
# cuenta los siguiente:
# ◦ Si se cumple Pitágoras entonces es triángulo rectángulo
# ◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
# ◦ Si los 3 lados son iguales entonces es equilátero.
# ◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.

"""
TERMINAR----------------------------------------------------------------

 cateto_A = int(input("Indica la medida del cateto A: "))
cateto_B = int(input("Indica la medida del cateto B: "))
cateto_C = ((cateto_A **2 + cateto_B **2) **0.5)
print(cateto_C) """

# 11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
# número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
# por 400.

""" año = int(input("Indica el año a comprobar: "))
if año % 4 ==0 and año % 100 !=0 and año % 400 == 0 :
	print("Es un año bisiesto")

else:
	print("El año no es bisiesto")
	
""" """ elif (año % 400 == 0):
	print("Es un año bisiesto")
elif año % 100 != 0:
	print("No es un año bisiesto") """ """ """

# 12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
# se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
# producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
# productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
# se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
# tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
# cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

# A = +0.20 si es de tamaño 1 / +0.30 si es de tamaño 2
# B = - 0.30 si es de tamaño 1 / - 0.50 si es de tamaño 2

""" tipo = str(input("Introduce el tipo de uva: "))
tamaño = float(input("Introduce el tamaño de la uva: "))
precio = float(input("El precio de la uva es de: "))

if tipo == "A" and tamaño == 1 :
	print("La ganancia obtenida es de:",precio + 0.20,)

elif tipo == "A" and tamaño == 2 :
	print("La ganancia obtenida es de:",precio + 0.30,)

elif tipo == "B" and tamaño == 1 :
	print("La ganancia obtenida es de:",precio - 0.30,)

elif tipo == "B" and tamaño == 2 :
	print("La ganancia obtenida es de:",precio - 0.50,)

else:
	print("Los datos introducidos son erróneos") """

# 13. El director de una escuela está organizando un viaje de estudios, y requiere determinar
# cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
# servicio. 
# La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
# alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
# y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
# número de alumnos. 
# Realice un algoritmo que permita determinar el pago a la compañía de
# autobuses y lo que debe pagar cada alumno por el viaje.

""" alumnos = int(input("Indique el número de alumnos que asistiran: "))

if alumnos >= 100:
	print("Cada alumno deberá pagar 65 € y la compañía recibirá", alumnos * 65)
elif alumnos >= 50 and alumnos <= 99:
	print("Cada alumno deberá pagar 70 euros y la compañía recibirá", alumnos * 70)
elif alumnos >= 30 and alumnos <= 49:
	print("Cada alumno deberá pagar 95 euros y la compañía recibirá", alumnos * 95)
elif alumnos <= 30:
	print("El costó de la renta del autobús es de 4000 € en total") """

# 14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
# es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
# los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
# décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
# es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
# determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

# 15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
# correspondiente. Si introducimos otro número nos da un error.

# 16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
# días que tiene el mes correspondiente.

# 17. Escribir un programa que imprima todos los números pares entre dos números que se le
# pidan al usuario

""" numero1 = int(input("Indicame el primer número: "))
numero2 = int(input("Indicame el segundo número: "))

numeroMenor = 0
segundoNumero = 0

if numero1 < numero2:
	numeroMenor = numero1
	segundoNumero = numero2
elif numero1 > numero2:
	numeroMenor = numero2
	segundoNumero = numero1

for i in range (numeroMenor, segundoNumero):
	if i %2 == 0:
		print(i)
 """
# 18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
# inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
# el programa dará las siguientes informaciones:
# ◦ La suma de los números que están dentro del intervalo (intervalo abierto).
# ◦ Cuantos números están fuera del intervalo.
# ◦ Informa si hemos introducido algún número igual a los límites del intervalo.

limInferior = int(input("Indica el límite inferior: ")) 
limSuperior = int(input("Indica el límite superior: "))
suma = 0
coincidencia = 0
nFuerainter = 0
while limInferior > limSuperior:
	limSuperior = int(input("Indica el límite superior: "))

numero = int(input("Introduce un número: "))
while numero != 0:
	if numero > limInferior and numero < limSuperior:
		suma += numero

	if numero == limInferior or numero == limSuperior:
		coincidencia += 1

	if numero < limInferior or numero > limSuperior:
		nFuerainter += 1

		print(f"la suma de los números que están dentro del intervalo es: {suma}")
		print(f"La cantidad de números que están fuera del intervalo es: {nFuerainter}")
		print(f"El número que coincide con los límites del intervalo es: {coincidencia}") 

# 19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
# (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
# de potencia.

""" nReal = int(input("Introdue un número real (base): "))
ePositivo = int(input("Introduce un número entero (exponente): "))

for potencia in range(nReal,0,ePositivo):
	print(potencia)

while ePositivo > 0:
 if potencia = nReal * ePositivo:
 print(potencia)
 """
base = int(input("Introduce la base: "))

exponente = int(input("Introduzca un exponente: "))

while exponente <0:
	exponente = int(input("Introduce el exponente"))

resultado = 1

for i in range (exponente):
	 resultado *= base

print(f"El resultado con for es {resultado}")

resultado = 1


# 20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
# segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
# cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.

""" for i in range(0,21,20):
	print(i)  """

pago_mes_1 = 10
pago_total = pago_mes_1

for i in range(2,21):
	pago_por_mes = pago_mes_1 * (2 ** (i-1))
	pago_total += pago_por_mes
	print(f"el pago por mes {i} es: {pago_por_mes} euros")

print(f"Total pagado tras los 20 meses: {pago_total}")

# 21. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
# números primos que queremos mostrar









