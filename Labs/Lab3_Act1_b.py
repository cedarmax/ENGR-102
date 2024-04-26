# By submitting this assignment, all team members agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 3, Activity 1b
# Date:           20 September 2019

#The team found the conversions formulas on the internet,
#We then constructed the input request to be stored in the appropriate variable.
 
from math import *

print('This program converts the number of BTUs to Joules')
BTUs=float(input('Please enter the number of BTUs to be converted to Joules:'))
Joules='%.4f'%(BTUs*1055.06)  #Conversion is 1 BTU = 1055.06 Joules.
print(BTUs, 'BTUs is equivalent to', Joules, 'Joules')