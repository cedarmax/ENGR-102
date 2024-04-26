# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 3b Activity 4 Program 1c
# Date:           20 September 2019

from math import *

#Mohr-Coulomb failure criterion
# (normal stress * tangent of angle of internal friction) + cohesion
print("This program calculates the Mohr-Coulomb failure criterion, given the normal stress, angle of internal friction, and cohesion.")
normalStress = float(input("Please enter the normal stress in lbf/in^2: ")) #(lbf/in^2)
angle = float(input("Please enter the angle of internal friction in radians: "))
slope = tan(angle) #the slope of the failure envelope
cohesion = float(input("Please enter the cohesion in lbf/in^2: ")) #(lbf/in^2)
mohr = (normalStress * slope)+ cohesion
print("The Mohr-Coulomb Failure Criterion when normal stress of", normalStress, "lbf/in^2 is applied to a material with cohesion", cohesion, "lbf/in^2 and angle of internal friction of", angle, "radians is", '%.4f'%(mohr),".")