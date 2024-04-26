# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     CFU01
# Date:           11 September 2019

#Declaration of values from the PDF:
length = 3.2 #inches
height = 7.6 #centimeters
breadth = 5.0 #inches

#Conversion from English to Metric units:
height_converted = height / 2.54

#Formula: volume = height * length * breadth
volume = length * height_converted * breadth

#Variables were used instead of just typing the letters in the print statement.
#This was done so that the values can be more easily changed.

print("Welcome!  This program calculates the volume of a rectangular parallelepiped.")
print("If the length is 3.2 inches, the height is 7.6 centimeters, and the breadth is 5.0 inches, then the volume is", volume, "cubic inches.")
print("Note that there was no error in units!  This program actually converts all the lengths to inches.")