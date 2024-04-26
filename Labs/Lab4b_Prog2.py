# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 4b Program 2
# Date:           27 September 2019

#Reynolds number = V * d / v
#V = characteristic velocity of the flow (m/s)
#d = pipe diameter (m)
#v = fluid kinematic viscosity (m^2/s)

input("This program calculates the Reynolds number for pipe flow and reports whether the flow is laminar, in transition, or turbulent.  Press enter to continue.")

Ve = float(input("Please enter the characteristic velocity of the flow (m/s): "))
d = float(input("Please enter the pipe diameter (m): "))
vi = float(input("Please enter the fluid kinematic viscosity (m^2/s): "))

Re = Ve * d / vi

if Re < 2300:
	print("The flow is laminar.")
elif Re == 2300:
	print("The flow is on the border of laminar and being in transition between laminar and turbulent.")
elif 2300 < Re < 2900:
	print("The flow is in transition between laminar and turbulent.")
elif Re == 2900:
	print("The flow is on the border of being in transition between laminar and turbulent and being turbulent.")
elif 2900 < Re:
	print("The flow is turbulent.")
else:
	print("Unknown error has occurred.")