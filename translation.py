#Good for making ciphers AKA make passwords
import string

def numbersToLetters(str):
	#both of the translation args are same length to map chars
	strIn = "abcdefghijklmnopqrstuvwxyz1234567890" #characters
	numsIn = "1234567890!)@(#*$&%^{<}?.:;|]>[+=-~_" #mapped to these
	table = str.maketrans(strIn, numsIn) #creates mapping table
	return str.translate(table) #does the translating

def vowelMapping(str):
	strIn = "aeiou"
	vowelChange = "uaeoi"
	table = str.maketrans(strIn, vowelChange)
	return str.translate(table)

print(numbersToLetters("tuckat8825")) #tuckat8825 = ^{3!1^--|[ for example
print("Vowel mapping "+vowelMapping("cat"))