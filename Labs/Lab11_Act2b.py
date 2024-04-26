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
file_name = input('Enter the file you wish to open:')
file_name = file_name + '.txt'
n = int(input('How many dimensions does your graph have? :'))
yvalues = []
xvalues = []
for i in range(n):
	yvalues.append([])

with open(file_name) as f: 
	row = f.readlines()
	for line in row:
		l = line.split()
		var = True
		for i in range(n+1):   # loops through the till reacches dimensions asked for 
			if var: # skips first value because was already appended
				var = False
			else:
				yvalues[i-1].append(float(l[i])) # appends into proper list
		xvalues.append(float(l[0]))
# creates arrays
xvalues = np.array(xvalues) 
yvalues = np.array(yvalues)		

# interpolation function
def interpolation(x,y_sum,x_sum,xy,x_pow):
	"""
	
	param: x is the x variables
	param: y_sum is the sum of the y variables
	param: x_sum is the sum of the x variables
	param: xy is the sum of the product of the list
	param: x_pow is the sum of the x values squared
	
	The function will take in the parameters and plug them into the eqautions for the intercept and slope.
	It will find the variables to create the linear equation for each trendline.
	
	"""
	N = len(xvalues) # finds the length of the x values
	m =  ((N*xy)-(x_sum*y_sum))/((N*x_pow)-((x_sum)**2)) #finds slope
	b = ((y_sum)-(m*x_sum))/N #calculating for the y intercept
	y = m*x + b #equation for finding y
	return y
# function for the calulation that will be put into the intercept and slope equation
def calculations(x,n):
	"""
	
	param: x is the x value at which you are trying to find your linear estimation and will plug into the equation once it is found.
	param: n is the dimensions for your y values
	 
	The program will use x to enter into the equations created by the data given by the file and find your linear estimation.
	N will be used solely for the dimesnions of your y values
	
	"""
	y = np.array([x]) # creates and array holding the x coordinate to append the rest of  the y coordinates
	for i in range(n): # loops through the dimensions
		y_sum = sum(yvalues[i]) # finds the sum of the y values for each individual graph
		x_sum = sum(xvalues) # finds the sum of the x values
		xy = sum(xvalues*yvalues[i]) # finds the sum of the product of x and y
		x_pow = sum(xvalues**2) # sum of xvalues squared
		# appends to an array
		b = y	
		y = np.append(b,interpolation(x,y_sum,x_sum,xy,x_pow))
	return y

x = float(input('Enter an x value to find linear estimation: '))
print(calculations(x,n))










