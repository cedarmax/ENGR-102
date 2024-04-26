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
# Assignment:	Lab 9
# Date:		    14 10 2019

"""

from math import*
filename = input('Enter the name of your file with the values you listed:')
filename = filename + '.csv'
f = open(filename)
# best line fit equation
xvalues = [] # list of x values
yvalues = [] # list of y values
# the variables and names for the sums
x_sum = 0 # sum of x's
y_sum = 0  #sum of y's
xy = 0    # sum of product of x*y
xpow2 = 0 # sum of x**2
var = True  # variable to allow first line skipped
# loops through the file
for line in f:
    line = line.split()
    if var:    # skips first line
    	var = False
    else:  
        xvalues.append(int(line[0]))
        yvalues.append(int(line[1]))
print('x-values are:',xvalues) # prints list for x
print('y-values are:',yvalues) # prints list for y
x = float(input('Enter the x value you wish to find the y value for:'))
for i in range(len(xvalues)):
    x_sum += xvalues[i]
    y_sum += yvalues[i]
    xy += (yvalues[i] * xvalues[i])
    xpow2 += (xvalues[i])**2
N = len(xvalues) # finding the length of the x coordinates
m = ((N*xy)-(x_sum*y_sum))/((N*xpow2)-((x_sum)**2)) #finds slope
b = ((y_sum)-(m*x_sum))/N #calculating for the y intercept
y = m*x + b #equation for finding y
print('the y value for ',x,'is', y) # print statements with results
f.close()


























