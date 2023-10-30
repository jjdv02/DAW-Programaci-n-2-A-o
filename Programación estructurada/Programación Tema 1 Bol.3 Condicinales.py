# 1. Realizar un programa que lea un número entero por teclado e informe de si el número es par o impar (el cero se considera par).
"""numero = int(input("Introduzca un número: "))

if numero % 2 == 0:
	print("El número es par")

else:
	print("El número es impar")
 """

# 2. Realizar un programa que solicite dos números por teclado e imprima en pantalla si son iguales, el primero mayor que
# el segundo o el primero más pequeño que el segundo.
"""numero1 = int(input("Indique el primer numero: "))
numero2 = int(input("Indique el segundo numero: "))

if numero1 > numero2:
	print("el numero", numero1 , "es mayor que el numero", numero2)

elif numero1 < numero2:
	print("el numero", numero2 , "es mayor que el numero", numero1)

elif numero1 == numero2:
	print("Ambos números son iguales") """


# 3. Realizar un programa que lea un número por teclado. El programa debe
# imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
# mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
# deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
# el programa finaliza sin mostrar ningún mensaje.
""" numero = int(input("Introduce un número: "))

if numero % 2 == 0 and numero % 3 == 0:
	print("El número", numero ,"es múltiplo de 2")
	print("El número", numero ,"es múltiplo de 3")

elif numero % 2 == 0:
	print("El número", numero ,"es múltiplo de 2")

elif numero % 3 == 0:
	print("El número", numero, "es múltiplo de 3")

else:
	print("El número introducido no es múltiplo de 2 ni de 3") 
 """

# 4. Realizar un programa que lea la edad de una persona menor a 100 años e
# informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
# 29) o un adulto.
""" edad = int(input("Introduzca su edad: "))

if edad >= 0 and edad <= 12:
	print("Usted es un niño")

elif edad >= 13 and edad <= 17:
	print("Usted es un adolescente")

elif edad >= 18 and edad <= 29:
	print("Usted es un joven")

elif edad >= 30 and edad <= 100:
	print("Usted es un adulto")

elif edad > 100:
	print("La edad introducida no es válida") """


# 5. Realizar un programa que solicite 4 números e imprima la media de los
# números. También debe imprimir aquellos números que son superiores a la
# media.

""" numero1 = int(input("Introduzca el primer numero: "))
numero2 = int(input("Introduzca el segundo numero: "))
numero3 = int(input("Introduzca el tercer numero: "))
numero4 = int(input("Introduzca el cuarto numero: "))
media = (numero1 + numero2 + numero3 + numero4) / 4
print(media)

if numero1 > media:
	print("El numero", numero1, "es mayor a la media de los 4 números")

if numero2 > media:
	print("El numero", numero2, "es mayor a la media de los 4 números")

if numero3 > media:
	print("El numero", numero3, "es mayor a la media de los 4 números")

if numero4 > media:
	print("El numero", numero4, "es mayor a la media de los 4 números")

else:
	print("El número que ha introducido no es válido")  """


# 6. Realizar un programa que solicite un carácter por teclado e informe por
# pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
# mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.

""" caracter = str(input("Introduce una letra: "))

if caracter == "a" or caracter == "A":
	print("Es la primera vocal a")

elif caracter == "e" or caracter == "E":
	print("Es la segunda vocal e")

elif caracter == "i" or caracter == "I":
	print("Es la tercera vocal i")

elif caracter == "o" or caracter == "O":
	print("Es la cuarta vocal o")

elif caracter == "u" or caracter == "U":
	print("Es la quinta vocal u")
     
elif caracter == "b" or caracter == "B":
     print("Es la consonante b")
     
elif caracter == "c" or caracter == "C":
    print("Es la consonante c")

elif caracter == "d" or caracter == "D":
    print("Es la consonante d")

elif caracter == "f" or caracter == "F":
    print("Es la consonante f")

elif caracter == "g" or caracter == "G":
    print("Es la consonante g")

elif caracter == "h" or caracter == "H":
    print("Es la consonante h")

elif caracter == "j" or caracter == "J":
    print("Es la consonante j")

elif caracter == "k" or caracter == "K":
    print("Es la consonante k")

elif caracter == "l" or caracter == "L":
    print("Es la consonante l")

elif caracter == "m" or caracter == "M":
    print("Es la consonante m")

elif caracter == "n" or caracter == "N":
    print("Es la consonante n")

elif caracter == "ñ" or caracter == "Ñ":
    print("Es la consonante ñ")

elif caracter == "p" or caracter == "P":
    print("Es la consonante p")

elif caracter == "q" or caracter == "Q":
    print("Es la consonante q")

elif caracter == "r" or caracter == "R":
    print("Es la consonante r")

elif caracter == "s" or caracter == "S":
    print("Es la consonante s")

elif caracter == "t" or caracter == "T":
    print("Es la consonante t")

elif caracter == "v" or caracter == "V":
    print("Es la consonante v")

elif caracter == "w" or caracter == "W":
    print("Es la consonante w")

elif caracter == "x" or caracter == "X":
    print("Es la consonante x")

elif caracter == "y" or caracter == "Y":
    print("Es la consonante y")

elif caracter == "z" or caracter == "Z":
    print("Es la consonante z")

else:
    print("El carácter seleccionado no es una letra")
   """
	

# 7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C-Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
# pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
# siguientes reglas:
#  A los solteros o divorciados menores de 35 años, un 12%
#  Todas las personas mayores de 50 años, un 8.5%
#  A los viudos o casados menores de 35 años, un 11.3%
#  Al resto de casos se le aplica un 10.5%
""" 
EstadoCivil = "S", "C", "V", "D"
EstadoCivil = str(input("Introduzca su estado civil: "))
Edad = int(input("Introduzca su edad: "))

if (EstadoCivil == "S" and Edad <= 35) or (EstadoCivil == "D" and Edad <= 35):
     print("Debe aplicársele un 12% de retención")
     
elif EstadoCivil == "S" or EstadoCivil == "C" or EstadoCivil == "V" or EstadoCivil == "D" and Edad >= 50:
     print("Debe aplicársele un 8.5% de retención")

elif (EstadoCivil == "V" and Edad <= 35) or (EstadoCivil == "C" and Edad <= 35):
     print("Debe aplicársele un 11.3% de retención")

elif EstadoCivil != "S" or EstadoCivil != "C" or EstadoCivil != "V" or EstadoCivil != "D":
	 print("El término introducido no es válido")

     
else:
     print("Debe aplicársele un 10.5%") """


# 8. Realizar un programa que lea por teclado dos marcaciones de un reloj
# digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
# 23:59:59 e informe cual de ellas es mayor.
# Ejemplo:
# Hora 1: 12:35:37
# Hora 2: 12:38:36
# “Hora 2 es mayor”
""" Hora1 = int(input("Introduce la primera hora a comparar : "))
Hora2 = int(input("Introduce la segunda hora a comparar : ")) 

if Hora1 >= (00,00,00) or Hora1 <= (23,59,59) :
      print ("Hora1: ", Hora1)

if Hora2 >= (00,00,00) or Hora2 <= (23,59,59) :
      print ("Hora2: ", Hora2)

if Hora1 > Hora2:
      print("La hora 1 es mayor que la hora 2")

if Hora2 > Hora1: 
      print("La hora2 es mayor que la hora 1") """

""" hora1 = 8
minuto1 = 24
segundo1 = 42
hora2 = 4
minuto2 = 26
segundo2 = 49

if 0 <= hora1 <= 23 and 0 <= hora2 <=23 and 0 <= minuto1 <= 59 and 0 <= minuto2 <= 59 and 0<= segundo1 <= 59 and 0 <= segundo2:
    
    if hora1 < hora2:
        print("La segunda hora es la mayor")
    elif hora2 < hora1:
        print("La primera hora es la mayor")
    else:
        if minuto1 < minuto2:
            print("La segunda hora es la mayor")
        elif minuto2 <= minuto1:
            print("La primera hora es la mayor")
        else:
            if segundo1 < segundo2:
                print("La segunda hora es la mayor")
            elif segundo2 < segundo1:
                print("La primera hora es la mayor")
            else:
                print("Las dos horas son iguales")

else:
    print("Los datos no son válidos") """

# 9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
# porcentaje de rebaja que se aplicará sobre el precio original del producto se
# calcula de la siguiente forma:
#  Si el producto es de tipo A, independientemente de su precio se
# aplica un 7% de descuento.

#  Si el producto es de tipo C o bien el precio es inferior a 500€ se
# aplicará un porcentaje del 12% de descuento.

#  En el resto de casos se aplica un 9% de descuento.

# Realizar un programa que solicite los datos necesarios (tipo de producto y
# precio original) y calcule el precio rebajado. Debe comprobarse que los
# datos de entrada son correctos, y si no lo son mostrar un mensaje de error.

""" tipoproducto = str(input("Indique el tipo de producto seleccionado: "))
PrOriginal = int(input("Indique el precio original: "))

if tipoproducto == "A":
	print(PrOriginal - 0.07) 
	
elif tipoproducto == "C" or PrOriginal <= 500:
	print(PrOriginal - 0.12)
	
elif tipoproducto == "B":
	print(PrOriginal - 0.09)
	
elif tipoproducto != "A" or tipoproducto != "B" or tipoproducto != "C":
    print("El caracter introducido no es válido")

else:
	print("ERROR") """

# 10.Realizar un programa que lea un carácter y dos números enteros por
# teclado. Si el carácter leído es un operador aritmético, calcular la operación
# correspondiente, si es cualquier otro debe mostrar un error.

""" operador = input("Introduce un operador aritmético: ")
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if operador == "+":
    print(numero1 + numero2)

elif operador == "-":
    print(numero1 - numero2)

elif operador == "*":
    print(numero1 * numero2)

elif operador == "/":
    print(numero1 / numero2)

else:
    print("El termino introducido como operador aritmético no es válido")  """




