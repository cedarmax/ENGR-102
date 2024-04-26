# By submitting this assignment, all team members agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 3, Activity 1c
# Date:           20 September 2019

#The team found the conversions formulas on the internet,
#We then constructed the input request to be stored in the appropriate variable.
 
from math import *
           
print('This program converts the number of Pascals to mmHg')
Pascals=float(input('Please enter the number of Pascals to be converted to mmHg:'))
mmHg='%.4f'%(Pascals*0.00750062)  #Conversion is 1 Pascal = 0.00750062 mmHg.
print(Pascals, 'Pascals is equivalent to', mmHg, 'mmHg')