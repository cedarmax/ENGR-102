# By submitting this assignment, all team members agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 3, Activity 1a
# Date:           20 September 2019

#The team found the conversions formulas on the internet,
#We then constructed the input reuest to be stored in the appropriate variable.
 
from math import *

print('This program converts number of pounds to number of Newtons')
pounds=float(input('Please enter the number of pounds to be converted to Newtons:'))
Newtons='%.4f'%(4.448*pounds) #Conversion is 1 pound = 4.448 Newtons.
print(pounds, 'pounds is equivalent to', Newtons, 'Newtons')