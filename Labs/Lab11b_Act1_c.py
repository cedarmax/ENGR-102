# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 11b Activity 1c
# Date:           14 November 2019

#User inputs:
name_input = input("Please enter your name: ")
city_input = input("Please enter your city: ")
state_input = input("Please enter your state: ")
zip_input = input("Please enter your zip-code: ")
address_input = input("Please enter your address: ")
address_input_2 = input("Please enter the second line of your address, if applicable (press 'n' to decline a second line): ")

def postmaster(name, city, state, zip, address):
	'''this function prints a mailing label'''
	if address_input_2 == 'n': #if they have another address, it is simply stated by not pressing 'n'
		print(name)
		print(address)
		print("%s," % city, "%s" % state, zip) #%s to get rid of the spaces between the comma and city
	else:
		print(name)
		print(address)
		print(address_input_2)
		print("%s," % city, "%s" % state, zip)
		
	
postmaster(name_input, city_input, state_input, zip_input, address_input)