# By submitting this assignment, all team members agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 3, Activity 1e
# Date:           20 September 2019

#The team found the conversions formulas on the internet,
#We then constructed the input request to be stored in the appropriate variable.
 
from math import *

print('This program converts Miles per Hour to Meters per Second')
MPH=float(input('Please enter the number of Miles per Hour to be converted to Meters per Second:'))
MPS='%.4f'%(MPH*0.44704)
print(MPH, 'Miles per Hour is equivalent to', MPS, 'Meters per Second')