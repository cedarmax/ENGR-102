# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 5, Activity 2c
# Date:           4 October 2019

from math import *

x = 1/2 # will need to be user input in final version
a = .1

f1 = 8*cos(x/2)
f2 = tan(2*x + 3) - 3
f3 = 7*sin(x/3)
f4 = log(3.4)/x

print(a, b, c, d)

fa = ((8*cos((x+a)/2)) - a) / a

if fa > 1e10-6:
	x = 1/2
	a = .1
	fa = ((8*cos((x+a)/2)) - a) / a
	a /= 2
elif: