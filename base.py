def convert(inputValue:str, inputBase:str, outputBase:str) :
	
	#---------------Usage----------------#
	
	# This fonction converts a string which represents an integer value encoded with a base to another base
	
	#--------------Inputs----------------#
	
	#inputValue:str		-> The string which represents a integer value
	#inputBase:str		-> The input base declaration which contains all the digits of the base in order (decimal base = "0123456789", hexadecimal base = "0123456789ABCDEF")
	#outputBase:str		-> The output base declaration which works just as the input base
	
	#-------------Outputs----------------#
	
	#outputValue:str		-> The input value encoded with the output base

	#------------Declarations------------#
	
	intValue = 0
	outputValue = ""
	
	#-------------Algorithm--------------#
	
	inputValue = inputValue[::-1]
	for i in range(len(inputValue)) :
		intValue += inputBase.index(inputValue[i]) * (len(inputBase) ** i)
	while intValue > 0 :
		outputValue = outputValue + str(intValue % len(outputBase))
		intValue = intValue // len(outputBase)
		
	#---------------Return---------------#
	
	return outputValue[::-1]

#============================================#

def decode(inputValue:str, inputBase:str) :
	
	#---------------Usage----------------#
	
	#This fonction decodes a string which represents an integer value encoded with a base
	
	#--------------Inputs----------------#
	
	#inputValue:str		-> The string which represents a integer value
	#inputBase:str		-> The input base declaration which contains all the digits of the base in order (decimal base = "0123456789", hexadecimal base = "0123456789ABCDEF")
	
	#-------------Outputs----------------#
	
	#outputValue:str		-> The input value decoded

	#------------Declarations------------#
	
	outputValue = 0
	
	#-------------Algorithm--------------#
	
	inputValue = inputValue[::-1]
	for i in range(len(inputValue)) :
		outputValue += inputBase.index(inputValue[i]) * (len(inputBase) ** i)
		
	#---------------Return---------------#
	
	return outputValue
	
#============================================#

def encode(inputValue:int, outputBase:str) :
	
	#---------------Usage----------------#
	
	#This fonction encodes an integer value to a base
	
	#--------------Inputs----------------#
	
	#inputValue:int		-> The integer value
	#outputBase:str		-> The output base declaration which contains all the digits of the base in order (decimal base = "0123456789", hexadecimal base = "0123456789ABCDEF")
	
	#-------------Outputs----------------#
	
	#outputValue:str		-> The input value encoded with the output base

	#------------Declarations------------#
	
	outputValue = ""
	
	#-------------Algorithm--------------#
	
	while inputValue > 0 :
		outputValue = outputValue + str(inputValue % len(outputBase))
		inputValue = inputValue // len(outputBase)
		
	#---------------Return---------------#
	
	return outputValue[::-1]
