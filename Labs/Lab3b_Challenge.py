# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 3b Challenge
# Date:           20 September 2019

from math import *

x = float(1/7)
y = int(input("Please enter the number of digits you want 1/7 truncated to: "))
print(int((x*(10**y)))/(10**y))

#We essentially convert 1/7 to scientific notation and then convert it to an integer.  That way the digits after what we want are truncated.  Then we divide that number by that same 10**x number 
