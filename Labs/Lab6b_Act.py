# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell
# Section:        537
# Assignment:     Lab 6 Activity 2
# Date:           11 October 2019

print("This program calculates the stress for structural steel given the strain.")
strain = float(input("Please enter the strain (0.00-0.27): "))

#Young's Modulus = stress / strain
#For segment O - A,B, this is ~ 43 / 0.01
#Values:

Ox = 0
Oy = 0
ABx = 0.01
ABy = 43
Cx = 0.06
Cy = 44
Dx = 0.18
Dy = 60
Ex = 0.27
Ey = 56

if 0 <= strain <=0.01: #O to A,B
	#We use young's modulus as the slope instead of calculating it otherwise.
	#We will approximate a value based on the graph and calculate based on that.
	#in this case, we'll say that at strain = 0.01, stress = 43.
	m = 43 / 0.01
	x1 = Ox
	y1 = Oy
	stress = m * (strain - x1) + y1
	print("The stress is", stress)
elif 0.01 < strain <= 0.06:
	x1 = ABx
	y1 = ABy
	x2 = Cx
	y2 = Cy
	m = (y2 - y1) / (x2 - x1)
	stress = m * (strain - x1) + y1
	print("The stress is", stress)
elif 0.06 < strain <= 0.18:
	x1 = Cx
	y1 = Cy
	x2 = Dx
	y2 = Dy
	m = (y2 - y1) / (x2 - x1)
	stress = m * (strain - x1) + y1
	print("The stress is", stress)
elif 0.18 < strain <= 0.27:
	x1 = Dx
	y1 = Dy
	x2 = Ex
	y2 = Ey
	m = (y2 - y1) / (x2 - x1)
	stress = m * (strain - x1) + y1
	print("The stress is", stress)
else:
	print("The strain is not within the domain of the graph.")