# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        ENGR 102-537
# Assignment:     Lab 10b Activity 1
# Date:           8 November 2019

from numpy import array
from matplotlib import pyplot

v = array([[1],[0]]).reshape(2,1)
M = array([[1.00583, -0.087156],[0.087156, 1.00583]]).reshape(2,2)
count = 0
x = array([1])
y = array([0])

while count < 200:
	v_new = (M @ v)
	pyplot.plot(v_new)
	v = v_new
	count += 1
pyplot.xlabel("X-axis")
pyplot.ylabel("Y-axis")
pyplot.title("Results of M @ v over 200 successive attempts (forms a triangle)")
pyplot.show()