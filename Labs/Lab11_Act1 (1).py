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
def f(x): # calls the original function
	"""
	param: x: what x value you want to find the y value for 
	
	The f(x) inputs your value into the original equation.
	the equation is y = 2x^3 +2x +3
	x^4 + x^2 + 3x -393
	"""
	y = (x**4)+(x**2) + 3*x - 393
	return y
def deriv(x): # finds the derivative of the funciton 
	"""
	
	param: x: takes the x value of where you are wanting to find the function and gets the derivitave
	
	The deriv(x) finds the derivative of the original function using the derivative equation.
	The function uses the formula y = (f(x+a)-f(x))/a 
	
	"""
	a = 0.1 # what the derivative divides by
	Tol = 1e-6 # the tolerance
	while a >= Tol: # loop for when a is not less than tolerance
		y = (f(x+a) - f(x))/(a) # derivative function
		a = a/2 # a constantly divides by two until less than tolerance
	return y
def newton_step(x): # fucntion for newton steps
	"""
	
	param: x: takes in the x value and plugs into every function that is called to use newton steps for finding roots
	
	newton_step that performs one step of Newton’s method.  Using the functions F and deriv, 
	newton_step should take as input a guess at a root, xi, and should return a new guess for
    the root, xi+1.   
	the equation is the graph being put into new_guess = initial guess - (x in the function )/(x in the derivative)
	
	"""
	new_guess = x-((f(x)/(deriv(x))))  # equation that finds the new guess using derivative and function of x
	return new_guess

def newton(x): # function for finding the root
	"""
	
	param: x takes in the x value that is the intial guess that tries to find the root using newton method
	
	newton that will take an initial guess for a root, x0, and will compute a sequence of root approximations. 
	The function should create and return a list of successive approximations to a root. 
	It can stop when the difference between
	successive approximations is no more than 10-6.   
	
	"""
	Tol = 1.0e-6 # tolerance 
	xi = newton_step(x)  # new intial guess
	sequ = [] # holds the guesses
	while abs(xi - x) >= Tol: # while loop for when the difference between the guesses is greater than tol
		sequ.append(xi) # appends each guess to sequ lsit
		x = xi # x is old guess
		xi = newton_step(x)	# creates new intital guess again
	return sequ
initial_guess = float(input('What is your initial guess for the root of the function?:'))
print(newton(initial_guess))

























