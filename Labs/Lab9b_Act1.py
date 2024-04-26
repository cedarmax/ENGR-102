# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell
# Section:        537
# Assignment:     Lab 9b Activity 1
# Date:           1 November 2019

CelsiusTemps = open('Celsius.dat')
contents = CelsiusTemps.read().split('\n')
CelsiusTemps.close()

#Creating a list of celsius temperatures so allow conversion to integer.  
#Otherwise, the '\n' is included and cannot be converted to integer.

FahrenheitCombined = '' #Empty string for all temps to be added to
#Not a list because lists cannot be written to files

for line in contents: #Take each temp and convert to fahrenheit
	FahrenheitTemp = str((int(line) * (9/5)) + 32) + '\n'
	FahrenheitCombined += FahrenheitTemp

FahrenheitDat = open('Fahrenheit.dat', 'w')
FahrenheitDat.write(FahrenheitCombined) #This is writing the string with every F value interspaced by '\n'
FahrenheitDat.close()

print("Done")