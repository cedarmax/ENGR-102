# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar James Maxwell
# Section:        102-537
# Assignment:     Lab 12b
# Date:           22 November 2019

import turtle as t
from math import sqrt

tallycount = int(input("Please enter the number to be represented in tally marks: "))

def tallymarks(tallycount):
	'''Represents a given integer in tally marks'''
	t.up()
	t.setpos(0, 100) #Choosing arbitrary position, (0,100) seems good
	t.right(90)
	x = 0 #Counter variable also used for x coordinate
	y = 100 #Actual y position
	for i in range(1, tallycount + 1):
		if (i % 5 == 0): #This is the diagonal line
			t.right(135)
			t.forward(30*sqrt(2))
			t.right(225)
		else: #For regular tallies
			t.up()
			t.goto(x*10, y)
			t.down()
			t.forward(30)
		x += 1
		if x >= 25: #This creates a new row
			t.up()
			y -= 80
			t.setpos(0, y)
			t.down()
			x = 0
	input() #Prevents window from disappearing
	
tallymarks(tallycount)