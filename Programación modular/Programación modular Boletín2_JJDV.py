# 1. Design a method called computeFactorial that receives a positive integer and
# returns the factorial for that number. If the number is negative the method should
# return None.

""" positiveInteger = 5

def computeFactorial(positiveInteger):
    if positiveInteger < 0:
        print("None")
     """

# 2. Design a method called isLeapYear that receives a number and returns False for
# common years and True for leap years. You may know that a year is considered to
# be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
# leap year if it is divisible by 100 unless it is also divisible by 400.

""" def esAnioBisiesto(anio):

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio_a_verificar = 2024
resultado = esAnioBisiesto(anio_a_verificar)

if resultado:
    print(f"{anio_a_verificar} es un año bisiesto.")
else:
    print(f"{anio_a_verificar} no es un año bisiesto.")
 """

# 3. Design a method called computeDaysInMonth that returns the number of days for
# the month and year that are received as arguments. You may use the method
# leapYear above. If the values are not valid the method should return -1.



# 4. Design a method called getDayOfWeek that receives a list containing three integers
# (day, month and year) and returns the day of the week for that date (Monday,
# Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).
# You can use the following algorithm to get a number between 0 (Sunday) and 6
# (Saturday) corresponding to the day in the week for a given date:
# a = (14 - month) / 12
# y = year – a
# m = month + 12 * a – 2
# d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7

""" fecha = [5,4,2005]

dia_semana = ["domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] """

# 5. Design a method called powerIt that receives two integers and raises the first
# number to the second. You may use the product or recursion and check the values. If
# no exponent is provided the first number is raised to 0.

""" def powerIt(base, exponent=0):
    result = 1

    if exponent > 0:
        for i in range(exponent):
            result *= base
    elif exponent < 0:
        for i in range(abs(exponent)):
            result /= base

    return result

base_numero = 2
exponente_numero = 3
resultado = powerIt(base_numero, exponente_numero)

print(f"{base_numero} elevado a la {exponente_numero} es igual a: {resultado}")
 """

# 6. Design a method called getNumberOfDigits that receives one number (it can be
# real, integer, positive or negative) and should return the number of digits it contains. If
# the parameter is not valid the method should return None. Extend this function to
# other numeric systems (hexadecimal, decimal, binary, octal).



# 7. Design a method called isPrime that receives one integer positive number greater
# than 0 as parameter. The method should return True if the number is prime or False if
# not prime. If the parameter is not valid the method should return None.

""" def esPrimo(numero):
   
    if not isinstance(numero, int) or numero <= 0:
        return None

    if numero == 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False

    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True

numero_prueba = 17
resultado = esPrimo(numero_prueba)

if resultado is None:
    print("Entrada no válida.")
elif resultado:
    print(f"{numero_prueba} es un número primo.")
else:
    print(f"{numero_prueba} no es un número primo.")
 """

# 8. Design a method called solveSecondOrderEquation that receives three integer
# positive numbers corresponding to the coefficients of a second order equation
# (ax2+bx+c=0) and computes its possible solutions. If the parameters are not valid the
# method should return None.

  

# 9. Design a method called getPrimeDivisors that receives a positive number as a
# parameter and returns a list containing its prime divisors. If the parameter is not valid
# the method should return None.



# 10. Design a method called isFriendNumber that receives two positive numbers and
# returns True if the numbers are friends, False otherwise. Two numbers are
# considered to be friends if the sum of its divisors, except the given number, is equal
# to the second and vice versa.

""" numero1 = 220
numero2 = 284
divisoresnumero1 = []
divisoresnumero2 = []
suma_lista1 = 0
suma_lista2 = 0
def ObtenerDivisoresNumeros(numero):
    divisores = []
    for i in range(1,numero):
        if (numero % i) == 0:
            divisores.append(i)
    return divisores

def sumaElementos (lista):
    sumaTotal = 0
    for i in lista:
        sumaTotal += 1
    return sumaTotal

def sonNumerosAmigos(numero1,numero2):
    return sumaElementos(ObtenerDivisoresNumeros(numero1)) == numero2 and sumaElementos(ObtenerDivisoresNumeros(numero2)) == numero1

print(ObtenerDivisoresNumeros(220))
print(sumaElementos(ObtenerDivisoresNumeros(220))) """
        