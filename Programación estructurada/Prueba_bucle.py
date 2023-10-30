""" for i in range (5, 51, 5):
	print(f"5 x {i} = ",i,) """

""" for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}") """

numero = int(input("Dime el número del que quieres la tabla de multiplicar: "))
while numero <= 0:
	numero = int(input("Dime el número del que quieres la tabla de múltiplicar: "))


indice = 1
while indice < 11:
	print(f"{numero} x {indice} es {numero * indice}") 
	indice += 1