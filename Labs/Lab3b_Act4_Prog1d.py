# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 3b Activity 4 Program 1d
# Date:           20 September 2019

#Arps equation
# q(t) = qi/(1+b*Di*t)^1/b
print("This program calculates the production rate of an oil well on a certain day given the initial production rate, the initial decline rate, and the hyperbolic constant.")
initialProduction = float(input("Please enter the initial production rate (units of barrles per day): ")) #initial production (qi)
initialDecline = float(input("Please enter the inital decline rate (units of barrels per day): ")) #initial decline rate (Di)
hyperbolicConstant = float(input("Enter the hyperbolic constant: ")) #hyperbolic constant (b)
time = float(input("Enter the number of days since production began: ")) #time since production (t)
productionRate = initialProduction/((1+hyperbolicConstant*initialDecline*time)**(1/hyperbolicConstant))
print("The production rate of a well with an intial production rate of", initialProduction, "barrels/day, an initial decline rate of", initialDecline, "barrels/day, and a hyperbolic constant of", hyperbolicConstant, "is", '%.4f'%(productionRate), "barrels/day.")