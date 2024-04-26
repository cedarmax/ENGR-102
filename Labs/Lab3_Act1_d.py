# By submitting this assignment, all team members agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 3, Activity 1d
# Date:           20 September 2019

#The team found the conversions formulas on the internet,
#We then constructed the input request to be stored in the appropriate variable.
 
from math import *

print('This program converts the number of seconds per revolution to Hz')
secs_per_rev=float(input('Please enter the number of seconds per revolution to be converted to Hz:'))
Hz='%.4f'%(1/secs_per_rev)
print(secs_per_rev, 'Number of seconds per revolution is equivalent to', Hz, 'Hz')