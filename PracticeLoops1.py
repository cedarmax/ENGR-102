# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:13:02 2019

@author: tlf719
"""

print('Code to estimate ln(1-x)')

x = float(input('Enter x: '))
numTerms = int(input('Enter number of terms: '))
sum = 0.0
for n in range(1, numTerms+1):
    sum = sum - (x**n)/n
    print('n = %2d   term = %10.8f' % (n, (x**n)/n))

print()
print('Estimate for ln(1-x) for x = %4.3f is %10.8f' % (x, sum))


#============================================================================
x = float(input('Enter x: '))
TOL = float(input('Enter desired tolerance: '))
sum = 0.0
 
# first term
n=1
term = x
 
sum = -term
 
while term > TOL:
     n = n + 1
     term = (x**n)/n
     sum = sum - term
     print('sum = %f   term = %f' % (sum, term))
print('Estimate for ln(1-x) for x = %4.3f is %10.8f' % (x, sum))
# =============================================================================

