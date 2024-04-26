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
print('This program will will store variables for a graph into a file.')
file_name = str(input('enter name of file:')) # name of file
fileName = file_name + '.csv'
with open(fileName,'w') as file:
    ind_var = str(input('What will be the independent variable for this file:'))
    dep_var = str(input('What will be the dependent variable for this file:'))
    file.write('%s' % ind_var.ljust(10))
    file.write('%s\n' % dep_var.ljust(10))
    print('Enter the independant and dependant variables. Enter stop when you\'re done.')
    coord1 = str(input('Enter your indpendent variable:'))    
    while coord1 != 'stop':
        coord2 = str(input('Enter your dependent variable:'))
        file.write('%s' % coord1.ljust(10))
        file.write('%s\n' % coord2.ljust(10))
        coord1 = str(input('Enter your indpendent variable:'))











































