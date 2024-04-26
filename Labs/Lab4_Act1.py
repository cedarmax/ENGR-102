# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell, David Simpson, and Muhammad Amer
# Section:        537
# Assignment:     Lab 4 Activity 1
# Date:           27 September 2019

from math import *

# define tolerance
TOL = 1e-10

a = 1/7
print(a)
b = a * 7
print(b)
c = 2 * a
d = 5 * a
e = c + d
print(e)

# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
	print('b and e are equal within tolerance of', TOL)
else:
	print('b and e are NOT equal within tolerance of', TOL)

x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)

if abs(z-x) < TOL:
	print('z and x are equal within tolerance of', TOL)
else:
	print('z and x are NOT equal within tolerance of', TOL)