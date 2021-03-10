import string

def cipherize(str, shift):
	#makes a string which is all lowercase letters of the alphabet
	letters = string.ascii_lowercase
	#make a "mask", its all the letters translated
	# so this is letters[shift:] letters from the shift point to the end
	# then letters[:shift] letters from the beginning to the shift point
	# combine them and it makes a mask, letters shifted
	mask = letters[shift:] + letters[:shift]
	#str.maketrans takes 2 args; the first is the original key
	# the second is the letters deleted or translated
	# so it maps the original letters to the new letters made from
	# the mask
	#i.e. 'abcde' -> shift it 2 -> it becomes 'cdefg'
	table = str.maketrans(letters, mask)
	#return the str.translate makes the new translation from the 
	# newly mapped out translation
	return str.translate(table)

print(cipherize("tucker", 2))