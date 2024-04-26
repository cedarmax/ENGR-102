# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar James Maxwell, 828007623
# Section:        537
# Assignment:     Lab 2b Program 1
# Date:           15 September 2019

from math import*

print("Hello World!");
print("My name is Cedar Maxwell.") 
print("I graduated from Bishop Lynch High School in Dallas this year.")
print("I've enrolled in the A&M academy to being my college career.")
print("Now on to the math...")
print("")

#Ohm's Law, voltage = current * resistance
current = 5
resistance = 20
voltage = current * resistance
print("If a conductor has a resistance of 20 ohms and a current of 5 amperes is run across it, the voltage is", voltage, "volts.")
print("")

#Kinetic Energy, 1/2*a*b^2
mass = 100
velocity = 21
kineticEnergy = .5*mass*(velocity**2)
print("Kinetic energy in joules is defined by the equation 1/2mv^2.  If the mass of an object traveling at 21m/s is 100kg, then the kinetic energy is", kineticEnergy, "joules.");
print("")

#Reynolds Number (Re)
#(velocity*linear characteristic)/viscosity = reynolds number
velocity2 = 100
cld = 2.5 
viscosity = 1.2 #viscosity
reynoldsNumber = (velocity2 * cld)/viscosity
print("The Reynolds number for a fluid with velocity 100m/s, kinetic viscosity of 1.2m^2/s, and characteristic linear dimension of 2.5 meters is",reynoldsNumber,".")
print("")

#Arps equation
# q(t) = qi/(1+b*Di*t)^1/b
initialProduction = 100 #initial production (qi)
initialDecline = 2 #initial decline rate (Di)
hyperbolicConstant = 0.8 #hyperbolic constant (b)
time = 20 #time since production (t)
productionRate = initialProduction/((1+hyperbolicConstant*initialDecline*time)**(1/hyperbolicConstant))
print("The production rate of a well with an intial production rate of 100 barrels/day, an initial decline rate of 2 barrels/day, and a hyperbolic constant of 0.8 is", productionRate, "barrels/day.")
print("")

#Mohr-Coulomb failure criterion
# (normal stress * tangent of angle of internal friction) + cohesion
normalStress = 20 #(lbf/in^2)
angle = radians(35) #angle of internal friction
slope = tan(angle) #the slope of the failure envelope
cohesion = 2 #(lbf/in^2)
mohr = (normalStress * slope)+ cohesion
print("The Mohr-Coulomb Failure Criterion when normal stress of 20lbf/in^2 is applied to a material with cohesion 2lbf/in^2 and angle of internal friction of 35 degrees is", mohr,".")