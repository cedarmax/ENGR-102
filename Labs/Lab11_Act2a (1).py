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

def interpolation(x):
	x_sum = sum(xvalues)
	y_sum = sum(yvalues)
	N = len(xvalues)
	xy = sum(yvalues*xvalues)
	xpow2 = sum(xvalues**2)
	m =  ((N*xy)-(x_sum*y_sum))/((N*xpow2)-((x_sum)**2)) #finds slope
	b = ((y_sum)-(m*x_sum))/N #calculating for the y intercept
	y = m*x + b #equation for finding y
	return y
xvalues = []
yvalues = [] # list of y values
file_name = 'Lab11Act2PartA_TestData.txt .txt'   ## change to user input
with open(file_name) as f:	
	row = f.readlines()
	for line in row:	
		l = line.split()
		xvalues.append(float(l[0]))
		yvalues.append(float(l[1]))
x = float(input('Enter the x value you would like to find the coordinate of: '))
xvalues.sort()
xvalues = np.array(xvalues)
yvalues = np.array(yvalues)
y = interpolation(x)
print('the y value for %f is %f'%(x,y))







































