# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 7b Program 1
# Date:           18 October 2019

UserInput = ""
vowels = ['a','e','i','o','u']

while UserInput != 'stop': #This doesn't work as originally intended, but it keeps the program going, so I left it as is.
	UserInput = input("Please enter the word you would like converted to Pig Latin: ")
	if UserInput == 'stop':
		print("Program aborted.")
		break
	elif UserInput[0] == 'a' or UserInput[0] == 'e' or UserInput[0] == 'i' or UserInput[0] == 'o' or UserInput[0] == 'u' or UserInput[0] == 'A' or UserInput[0] == 'E' or UserInput[0] == 'I' or UserInput[0] == 'O' or UserInput[0] == 'U':
		UserInput += 'ay'
		print("Your word in Pig Latin is: ", UserInput.lower().title())
	else:
		UserInput += UserInput[0]
		UserInput = UserInput[1 : : ]
		UserInput += 'ay'
		print("Your word in Pig Latin is: ", UserInput.lower().title())