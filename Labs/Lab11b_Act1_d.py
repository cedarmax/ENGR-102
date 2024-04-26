# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 11b Activity 1d
# Date:           14 November 2019

#Input from user:
name_input = input("Please enter the name of the file (csv, no extension necessary): ")

def tsv_converter(name):
	'''this function converts a csv file to a tsv file''' #docstring :)
	name_csv = name + '.csv' #appending the appropriate file extensions
	name_tsv = name + '.tsv'
	tsv = []
	with open(name_csv, 'r') as table:
		contents = table.read().split('\n') #splitting in to each line
		for line in contents: 
			tsv_line = line.replace(',', '\t') #csv --> tsv (commas to tabs)
			tsv.append(tsv_line)
	with open(name_tsv, 'w') as table:
		for line in tsv:
			line.split('\n') #wouldn't work without doing this
			table.write(line + '\n') #readding \n 

tsv_converter(name_input)