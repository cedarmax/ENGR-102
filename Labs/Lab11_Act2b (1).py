# -*- coding: utf-8 -*-
"""
# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 		Erwin Luevano
#               Alex Torres
#	            Cedar Maxwell
#	            Muhammad Amer
# Section:		ENGR 102-537
# Assignment:	Lab 11
# Date:		    13 11 2019

"""

from math import*
import numpy as np
import matplotlib.pyplot as plt
#file_name = input('Enter the file you wish to open:')
#file_name = file_name + '.txt'
#dim = int(input('How many dimensions does your graph have? :'))
yvalues = []
xvalues = []
n = 3
for i in range(n):
	yvalues.append([])
"""
Add user inputs of file name, n, and x
"""
file_name = 'Lab11Act2PartB_TestData.txt'
with open(file_name) as f:
	row = f.readlines()
	for line in row:
		l = line.split()
		var = True
		for i in range(n+1):   # will change to range of dim!!!!!!
			if var:
				var = False
			else:
				yvalues[i-1].append(float(l[i]))
		xvalues.append(float(l[0]))
xvalues = np.array(xvalues)
yvalues = np.array(yvalues)		

def interpolation(x,y_sum,x_sum,xy,x_pow):
	N = len(xvalues)
	m =  ((N*xy)-(x_sum*y_sum))/((N*x_pow)-((x_sum)**2)) #finds slope
	b = ((y_sum)-(m*x_sum))/N #calculating for the y intercept
	y = m*x + b #equation for finding y
	return y
def calculations(x,n):
	y = np.array([x])
	for i in range(n):
		y_sum = sum(yvalues[i])
		x_sum = sum(xvalues)
		xy = sum(xvalues*yvalues[i])
		x_pow = sum(xvalues**2)	
		b = y	
		y = np.append(b,interpolation(x,y_sum,x_sum,xy,x_pow))
	return y


print(calculations(3,n))










