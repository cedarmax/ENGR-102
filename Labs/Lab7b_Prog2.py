# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 7b Program 2
# Date:           18 October 2019

from math import *

dimension = int(input("Please enter the number of dimensions:")) #Same dimension for both vectors

#Empty lists created so that they can be appended
A = []
B = []
sum = []
difference = []
product = []
magnitude_A = 0
magnitude_B = 0

for i in range(dimension):
	userInputA = float(input("Please enter vector A value: "))
	A.append(userInputA) #Adds values to list

for i in range(dimension):
	userInputB = float(input("Please enter vector B value: "))
	B.append(userInputB)
	
for i, j in enumerate(A): #enumerate allows comparison between the two lists in one for loop
	add = j + B[i]
	sum.append(add)
	subtract = j - B[i]
	difference.append(subtract)
	multiply = j * B[i]
	product.append(multiply)
	magnitude_A += j**2
	magnitude_B += B[i]**2

print("The magnitude of A is:", sqrt(magnitude_A)) #square root is done here because it cannot be included in the for loop,
print("The magnitude of B is:", sqrt(magnitude_B)) #otherwise all the individual values would be square-rooted.
print("The dot product of A and B is:", product)
print("A + B =", sum)
print("A - B =", difference)