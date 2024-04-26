# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell, David Simpson, Mohammed Amer
# Section:        537
# Assignment:     Lab 7 Activity 2
# Date:           18 October 2019

from math import *

#Part A

x = 0

gradeData=[79,99,73	,49,67,62,52,99,57,58	,67,88,71	,69,41,74	,53,90,63	,
           66,92,54	,61,59,48,71,83,89,99	,69,66,40,48,41,99,68	,52,78,77,
           71,40,65,77,87,96,44,54,60,89,72]

for i in gradeData:
	x += i
average = x / len(gradeData)
print("The average grade is:", average)

#Part B

xbar = average

stdev = sqrt(sum((x - xbar)**2 for x in gradeData) / len(gradeData))
print("The standard deviation is:", stdev)

#Part C

max = 0

for i in gradeData:
	if i > max:
		max = i
print("The max is:", max)

min = 10000

for i in gradeData:
	if i < min:
		min = i
print("The min is:", min)

#Part D

deltaGrade = 0
y = 0

xbar = x / len(gradeData)

#This works for within a tolerance of 1e-5.  1e-6 took to long to calculate.
while xbar < 75.0:
	xbar = x / len(gradeData)
	deltaGrade += .00001
	for i in gradeData:
		i += .00001
		x += .00001
		xbar = x / len(gradeData)
# print(i)
# print(x)  #for testing purposes
# print(xbar)
print("The constant deltaGrade needed to be added to each score to create an average of 75.0 within a tolerance of 1e-5 is", deltaGrade)