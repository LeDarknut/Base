#============================================#

	#---------------Usage----------------#
	
	# This fonction converts a string which represents an integer value encoded with a radix to another radix
	
	#--------------Inputs----------------#
	
	#inputValue:str		-> The string which represents a integer value
	#inputRadix:str		-> The input radix declaration which contains all the digits of the radix in order (binary radix = "01", decimal radix = "0123456789", hexadecimal radix = "0123456789ABCDEF")
	#outputRadix:str	-> The output radix declaration which works just as the input radix
	
	#-------------Outputs----------------#
	
	#outputValue:str	-> The input value encoded with the output radix
	
#============================================#
	
def convert(inputValue:str, inputRadix:str, outputRadix:str) :
	intValue = 0
	outputValue = ""
	inputValue = inputValue[::-1]
	for i in range(len(inputValue)) :
		intValue += inputRadix.index(inputValue[i]) * (len(inputRadix) ** i)
	while intValue > 0 :
		outputValue = outputValue + str(intValue % len(outputRadix))
		intValue = intValue // len(outputRadix)
	return outputValue[::-1]



#============================================#

	#---------------Usage----------------#
	
	#This fonction decodes an integer value encoded with a radix
	
	#--------------Inputs----------------#
	
	#inputValue:str		-> The string which represents an integer value encoded with a radix
	#inputRadix:str		-> The input radix declaration which contains all the digits of the radix in order (binary radix = "01", decimal radix = "0123456789", hexadecimal radix = "0123456789ABCDEF")
	
	#-------------Outputs----------------#
	
	#outputValue:str	-> The input value decoded

#============================================#

def decode(inputValue:str, inputRadix:str) :
	outputValue = 0
	inputValue = inputValue[::-1]
	for i in range(len(inputValue)) :
		outputValue += inputRadix.index(inputValue[i]) * (len(inputRadix) ** i)
	return outputValue



#============================================#

	#---------------Usage----------------#
	
	#This fonction encodes an integer value with a radix
	
	#--------------Inputs----------------#
	
	#inputValue:int		-> The integer value
	#outputRadix:str	-> The output radix declaration which contains all the digits of the radix in order (binary radix = "01", decimal radix = "0123456789", hexadecimal radix = "0123456789ABCDEF")
	
	#-------------Outputs----------------#
	
	#outputValue:str	-> The input value encoded with the output radix

#============================================#

def encode(inputValue:int, outputRadix:str) :
	outputValue = ""
	while inputValue > 0 :
		outputValue = outputValue + str(inputValue % len(outputRadix))
		inputValue = inputValue // len(outputRadix)
	return outputValue[::-1]
