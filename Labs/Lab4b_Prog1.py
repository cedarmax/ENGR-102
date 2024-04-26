# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 4b Program 1
# Date:           27 September 2019

input("This program takes 3 floating point values and determines which the largest.  Press enter to continue.")

#Creation of variables for user input
x = float(input("Please enter a number for 'x': "))
y = float(input("Please enter a number for 'y': "))
z = float(input("Please enter a number for 'z': "))

#Loops defining for behavior for x condition:
if x > y and x > z:
	print("x is the largest number:", x)
elif y > x and y > z:
	print("y is the largest number:", y)
elif z > x and z > y:
	print("z is the largest number:", z)
elif x > z and y > z:
	print("x and y are larger than z:", x, "and", y, ",", "respectively.")
elif z > y and x > y:
	print("z and x are larger than y:", z, "and", x, ",", "respectively.")
elif y > x and z > x:
	print("y and z are larger than x:", y, "and", z, ",", "respectively.")
elif y==x or y==z or x==z or x==y:
	print("No number is greater than all the others.")
else:
	print("Catastrophic error has occurred!")