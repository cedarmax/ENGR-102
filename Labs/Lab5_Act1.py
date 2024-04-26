# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell, David Simpson, Muhammad Amer
# Section:        537
# Assignment:     Lab 5
# Date:           4 October 2019

from math import *
x = 0
f_x= x**3 - x**2 - 4*x + 4

if f_x > 0.000001 or f_x < 0.000001:
	while f_x > 0.000001:
		x = x + 0.0001
		f_x= x**3 - x**2 - 4*x + 4
		print(f_x)
	while f_x < 0.000001:
		x = x - 0.0001
		f_x= x**3 - x**2 - 4*x + 4
		print(f_x)
	print(f_x)
else:
	print(f_x)