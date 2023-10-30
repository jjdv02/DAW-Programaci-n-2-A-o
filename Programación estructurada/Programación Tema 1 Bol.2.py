
""" # 1. Escribir una expresión lógica que cumpla:
# a. Debe ser Verdadera si el contenido de las variables enteras sueldo_bruto y
# sueldo_neto es el adecuado para una retención del 22%.
sueldobruto = 2000
sueldoneto = 1560
print(sueldoneto==sueldobruto - (sueldobruto*0.22))

# b. Debe ser Verdadera si el contenido de la variable entera día es un valor válido para
# el mes de mayo.
dia = 4
print(dia >= 1 and dia <= 31)

# c. Debe ser Verdadera si el número contenido en las variables enteras num1 y num2
# son múltiplos de tres.
num1 = 3
num2 = 21
print(num1 % 3 == 0 and num2 % 3 == 0  )

# d. Debe ser Verdadera si la calificación contenida en la variable real nota es un
# aprobado.
nota = 6
print(nota >= 5 and nota <= 10)

# e. Debe ser Verdadera si la media de la calificación contenida en las variables reales
# nota1, nota2 y nota3 es un aproblado.
nota1 = 4
nota2 = 8
nota3 = 9
notamedia = nota1 + nota2 + nota3 / 3
print(notamedia >= 5) 

 
# 2. Escribir una expresión lógica que cumpla:
# a. Debe ser Falsa si alguna de las calificaciones contenidas en las variables reales
# nota1, nota2 y nota3 es un suspenso.
nota1 = 4
nota2 = 8
nota3 = 9
print(nota1 >= 5 and nota2 >= 5 and nota3 >= 5)


# b. Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga
# menos de 1000 euros en la variable saldo o se haya quedado al descubierto más de
# 5 veces. Este último dato se almacenará en la variable descubierto
saldo = 1400
descubierto = 6
print(saldo <= 1000 and descubierto <= 5)
"""
# c. Debe ser Falsa cuando el valor almacenado en la variable asignaturasAprobadas
# sea inferior al 30% del valor almacenado en la variable asignaturasCurso.
asignaturascurso = 7
asignaturasaprobadas = 2
print(asignaturascurso * 0.30 <= asignaturasaprobadas)

"""
# d. Debe ser Falsa si los números contenidos en las variables enteras mes y día no son
# válidos. Vamos a considerar que no hay años bisiestos.
# NOTA: Además siempre debe ser Verdadera en el caso contrario al que se formula

mes = 12
dia = 31

print((mes == 1 or mes == 2 or mes == 3 or mes == 4 or mes == 5 or mes == 6 or mes == 7 or mes == 8 or mes == 9 or mes == 10 or mes == 11 or mes == 12) and dia <= 31)

# 3. Determina para qué valores es cierta la siguiente expresión sin calcular su tabla de verdad. Comprueba el resultado en python:
"llueve y no haceSol y no haceFrio o no llueve y haceSol y no haceFrio o no llueve y no haceSol y haceFrio"



# 4. A partir de los dos enunciados siguientes, expresa en castellano el significado de las
# siguientes expresiones lógicas:
# a: Me gusta programar
# b: Voy a dedicar al menos diez horas a la semana a programar

# 1. not a and b
"No me gusta programar y voy a dedicar al menos 10 horas a la semana a programar"
# 2. not a or b
"No me gusta programar o voy a dedicar al menos 10 horas a la semana a programar"
# 3. not not a
"Me gusta programar"
# 4. not a or not b
"No me gusta programar o no me gusta dedicar al menos 10 horas a la semana a programar"
# 5. not (a or b)
"No me gusta programar o no voy a dedicar al menos 10 horas a la semana a programar"
# 6. not a and not b
"No me gusta programar y no me gusta dedicar al menos 10 horas a la semana a programar"
"""