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

import numpy as np
import matplotlib.pyplot as plt
print('Act 1')
def f(x):
	"""
	The f(x) inputs your value into the original equation.
	"""
	y = 2*(x**3)+2*(x) + 3
	return y
def deriv(x):
	"""
	The deriv(x) finds the derivative of the original function. 
	The function uses the formula 
	"""
	a = 0.1
	Tol = 1e-6
	while a >= Tol:
		y = (f(x+a) - f(x))/(a)
		a = a/2
	return y
def newton_step(x):
	"""
	newton_step that performs one step of Newton’s method.  Using the functions F and deriv, 
	newton_step should take as input a guess at a root, xi, and should return a new guess for
    the root, xi+1.   
	"""
	new_guess = x-((f(x)/(deriv(x))))
	return new_guess

def newton(x):
	"""
	newton that will take an initial guess for a root, x0, and will compute a sequence of root approximations. 
	The function should create and return a list of successive approximations to a root. 
	It can stop when the difference between
	successive approximations is no more than 10-6.   
	"""
	Tol = 1.0e-6
	xi = newton_step(x)
	sequ = []
	while abs(xi - x) >= Tol:
		sequ.append(xi)
		x = xi
		xi = newton_step(x)	
	return sequ
initial_guess = float(input('What is your initial guess for the root of the function?:'))
print(newton(initial_guess))

























