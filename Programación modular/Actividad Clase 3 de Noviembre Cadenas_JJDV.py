# 1. Design a function called charactersInString that has a character string and a character
# as input parameters and returns how many times that character appears in the string. It
# should do it no matter if the string and character are lower case or upper case characters.

def characterInString(cadena, caracter):
	numero = 0

	for i in cadena: 
		if i == caracter:
			numero += 1
	return numero

cadena = "Hola, Buenas tardes"
caracter = ("a")
devuelve = characterInString(cadena, caracter)
print(f"En la frase {cadena}, aparece la letra {caracter} {devuelve} vez/veces")


# 2. Design a function called lowCaseInString that has a string of characters as parameter,
# the method should return how many of those characters are lowercase letters.

