'''
#1. Calcular el resultado de las siguientes expresiones lógicas
"a"
print(7>=27 and not (7<=2))
"b"
print(24>5 and 10<=10 or 10==5)
"c"
print(10>=15 or 23==13) and not (8==8)
"d"
print(not (6//3>3) or 7>7)
'''
'''
# 2. Calcular el valor de las siguientes expresiones aritméticas:
"a"
print(27 % 4 + 15 / 4)
"b"
print(37/4**2-2)
"c"
print(9*2 / 3*10*3)
"d"
print((7*3-4*4)**2/4*2)

# 3. Escribir una expresión lógica que cumpla:

#a Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60
#euros pero igual o inferior a 420 euros.

Precio = 45
print(Precio >= 60 and Precio <= 420)

#b Debe ser Verdadera si el numero contenido en la variable entera numero es impar.

Numero = 2
print(Numero % 2 != 0)

#c Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son válidas.

Saldo = 20
DineroSacar = 10
print(Saldo>=0 and DineroSacar <= Saldo)

#d  Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que estén comprendidas entre 0:0 y 23:59.

hora = 21
minutos = 43
(hora >= 0 and hora <= 23) and minutos >= 0 and minutos <= 59

print((hora >= 0 and hora <= 23) and minutos >= 0 and minutos <= 59)

#e Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una persona no es correcta
#(S-Soltero, C-Casado, V-Viudo, D-Divorciado).
	
EstadoCivil = "s"
print(EstadoCivil != "s" and EstadoCivil != "c" and EstadoCivil != "v" and EstadoCivil != "d")

#4. Escribir una expresión lógica que cumpla:
#a Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero es superior a 300 euros o negativa.

cantidad = 205
print(cantidad <= 300 or cantidad <= 0 )

 #b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22 años.

edad = 18
print(not(edad >= 16 or edad <= 22))

 #c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
 
respuesta = "s"
print(not(respuesta =="s" or respuesta == "n"))

 #d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.

numero = 21

print(not(numero % 7 == 0 and numero % 3 == 0))
'''