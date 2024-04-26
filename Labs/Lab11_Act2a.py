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

def interpolation(x): # interpolation fucntion
	x_sum = sum(xvalues) # finds the sum of the xvalues
	y_sum = sum(yvalues) # finds the sum of the yvalues
	N = len(xvalues) # finds the length of the variables
	xy = sum(yvalues*xvalues) # finds the sum of the product of the x and y values
	xpow2 = sum(xvalues**2) # finds the sum of the xvalues to the power of 2
	m =  ((N*xy)-(x_sum*y_sum))/((N*xpow2)-((x_sum)**2)) #finds slope
	b = ((y_sum)-(m*x_sum))/N #calculating for the y intercept
	y = m*x + b #equation for finding y
	return y
xvalues = [] # lsit of x values
yvalues = [] # list of y values
file_name = input('Enter the file name which you would like to open: ')+ '.csv'  
with open(file_name) as f:	
	row = f.readlines() # reads lines in file
	for line in row:	 
		l = line.split() # splits data
		xvalues.append(float(l[0])) # appends to x values
		yvalues.append(float(l[1])) # appends to y values
x = float(input('Enter the x value you would like to find the coordinate of: ')) # enters the x in where youre finding the y
xvalues.sort()
 # creates arrays
xvalues = np.array(xvalues) 
yvalues = np.array(yvalues)
y = interpolation(x) # calls the function
print('the y value for %f is %f'%(x,y))







































