# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 4b Program 4
# Date:           27 September 2019

from math import *

print("This program solves the quadratic equation given coefficients A, B, and C.")

a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

#Quadratic formula is x = (-b +- sqrt(b^2 - 4ac))/2a

if ((b**2)-4*a*c) < 0:
#Split the formula in to two separate calculations.
#This is done to allow for a negative discriminant.
#Couldn't get it to work on one line for some reason.
	q = complex(((b**2)-4*a*c))
	y = (-b + q) / 2*a
	y2 = (-b - q) / 2*a
	print("The quadratic formula yields two potential values for x.  The values for x, in this case, are imaginary.")
	print("The first is:", y)
	print("The second is:", y2)
elif a == 0 and b != 0:
	print(-c / b)
elif a == b == 0 and c != 0:
	print("Because a and b are zero, c must be zero, but you have entered a non zero value for c.")
else:
	x = (-b + ((b**2)-4*a*c)) / 2*a
	x2 = (-b - ((b**2)-4*a*c)) / 2*a
	print("The quadratic formula yields two potential values for x.")
	print("The first is:", x)
	print("The second is:", x2)