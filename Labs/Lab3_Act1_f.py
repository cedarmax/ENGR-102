# By submitting this assignment, all team members agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 3, Activity 1f
# Date:           20 September 2019

#The team found the conversions formulas on the internet,
#We then constructed the input reuest to be stored in the appropriate variable.
 
from math import *

print('This program converts degrees Fahrenheit to degrees Celsius')
F=float(input('Please enter the degrees Fahrenheit to be converted to degrees Celsius:'))
C='%.4f'%((F-32)*(5/9)) #This is the forumla for the F to C conversion.
print(F, 'degrees F is equivalent to', C, 'degrees C')



