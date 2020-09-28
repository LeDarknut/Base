def convert(inputValue:str, inputRadix:str, outputRadix:str) :
	
	#---------------Usage----------------#
	
	# This fonction converts a string which represents an integer value encoded with a radix to another radix
	
	#--------------Inputs----------------#
	
	#inputValue:str		-> The string which represents a integer value
	#inputRadix:str		-> The input radix declaration which contains all the digits of the radix in order (decimal radix = "0123456789", hexadecimal radix = "0123456789ABCDEF")
	#outputRadix:str	-> The output radix declaration which works just as the input radix
	
	#-------------Outputs----------------#
	
	#outputValue:str	-> The input value encoded with the output radix

	#------------Declarations------------#
	
	intValue = 0
	outputValue = ""
	
	#-------------Algorithm--------------#
	
	inputValue = inputValue[::-1]
	for i in range(len(inputValue)) :
		intValue += inputRadix.index(inputValue[i]) * (len(inputRadix) ** i)
	while intValue > 0 :
		outputValue = outputValue + str(intValue % len(outputRadix))
		intValue = intValue // len(outputRadix)
		
	#---------------Return---------------#
	
	return outputValue[::-1]

#============================================#

def decode(inputValue:str, inputRadix:str) :
	
	#---------------Usage----------------#
	
	#This fonction decodes a string which represents an integer value encoded with a radix
	
	#--------------Inputs----------------#
	
	#inputValue:str		-> The string which represents a integer value
	#inputRadix:str		-> The input radix declaration which contains all the digits of the radix in order (decimal radix = "0123456789", hexadecimal radix = "0123456789ABCDEF")
	
	#-------------Outputs----------------#
	
	#outputValue:str	-> The input value decoded

	#------------Declarations------------#
	
	outputValue = 0
	
	#-------------Algorithm--------------#
	
	inputValue = inputValue[::-1]
	for i in range(len(inputValue)) :
		outputValue += inputRadix.index(inputValue[i]) * (len(inputRadix) ** i)
		
	#---------------Return---------------#
	
	return outputValue
	
#============================================#

def encode(inputValue:int, outputRadix:str) :
	
	#---------------Usage----------------#
	
	#This fonction encodes an integer value to a radix
	
	#--------------Inputs----------------#
	
	#inputValue:int		-> The integer value
	#outputRadix:str	-> The output radix declaration which contains all the digits of the radix in order (decimal radix = "0123456789", hexadecimal radix = "0123456789ABCDEF")
	
	#-------------Outputs----------------#
	
	#outputValue:str	-> The input value encoded with the output radix

	#------------Declarations------------#
	
	outputValue = ""
	
	#-------------Algorithm--------------#
	
	while inputValue > 0 :
		outputValue = outputValue + str(inputValue % len(outputRadix))
		inputValue = inputValue // len(outputRadix)
		
	#---------------Return---------------#
	
	return outputValue[::-1]
