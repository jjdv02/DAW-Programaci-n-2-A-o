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
devuelve = characterInString(cadena, caracter):
print(f"En la frase{cadena}, aparece la letra {caracter} {numero} vez/veces")


# 2. Design a function called lowCaseInString that has a string of characters as parameter,
# the method should return how many of those characters are lowercase letters.



# 3. Design a function called upperCaseInString that has a string of characters as parameter
# and the method should return how many are uppercase letters.

# 4. Design a function called numberInString that receives a string of characters as
# parameter and returns how many of them are numbers.

# 5. Design a function called palindrome that has a string of characters as input parameter,
# and returns True if it is a palindrome or False in other cases. A word is a palindrome if it
# can be read the same from left to right or right to left, ignoring whites. For example:
# "anilina" or "Dabale arroz a la zorra el abad" To simplify the problem, you can assume
# that simple characters are used, that is, without tildes or diresis.

# 6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo,
# si la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
# encontrará y deberá devolver True, en caso contrario deberá devolver False. Las letras
# de la palabra escondida deben aparecer en el orden correcto en la cadena que la oculta:
# shybaoxlna ⇒ hola: True
# soybahxlna ⇒ hola: False

# 7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase
# y deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla
# por la tercera.

# 8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una
# palabra o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.

# 9. Crear una función que, tomando una cadena de texto como entrada, construya y
# devuelva otra cadena formada de la siguiente manera: todas las consonantes estarán al
# principio y todas las vocales al final de la misma, eliminando los blancos. Por ejemplo,
# pasándole la cadena "curso de programacion", una posible solución sería
# "crsdprgrmcnuoeoaaio’.

# 10. Escribir una función que devuelva el número de palabras que hay en una cadena que
# recibe como parámetro. Ten en cuenta que entre dos palabras puede haber más de un
# blanco. También al principio y al final de la frase puede haber blancos redundantes. Por
# ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3.

