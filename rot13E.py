try:
	import string
	rot13 = string.maketrans( 
    		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    		"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	letter = raw_input("Please enter word or sentence for encryption:")
	print "The cipher will be :",string.translate(letter, rot13)

except:
	print "Error occured,try again"
