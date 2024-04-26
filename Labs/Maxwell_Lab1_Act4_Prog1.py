# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar James Maxwell
# Section:        537
# Assignment:     Lab 1b Program 1
# Date:           28 August 2019
from math import*

print("Hello World!");
print("My name is Cedar Maxwell.") 
print("I graduated from Bishop Lynch High School in Dallas this year.")
print("I've enrolled in the A&M academy to being my college career.")
print("Now on to the math...")
print("")

#Ohm's Law
x = 5 #current
y = 20 #resistance
z = x * y #voltage
print("If a conductor has a resistance of 20 ohms and a current of 5 amperes is run across it, the voltage is",z)
print("")

#Kinetic Energy
a = 100 #mass
b = 21 #velocity
c = .5*a*(b**2) #kinetic energy formula, 1/2*a*b^2
print("Kinetic energy in joules is defined by the equation 1/2mv^2.  If the mass of an object traveling at 21m/s is 100kg, then the kinetic energy is",c);
print("")

#Reynolds Number (Re)
#(velocity*linear characteristic)/viscosity = reynolds number
d = 100 #velocity (m/s)
e = 2.5 #characteristic linear dimension(m)
f = 1.2 #viscosity
g = (d * e)/f #reynolds number
print("The Reynolds number for a fluid with velocity 100m/s, kinetic viscosity of 1.2m^2/s, and characteristic linear dimension is",g)
print("")

#Arps equation
# q(t) = qi/(1+b*Di*t)^1/b
h = 100 #initial production (qi)
i = 2 #initial decline rate (Di)
j = 0.8 #hyperbolic constant (b)
k = 20 #time since production (t)
l = h/((1+j*i*k)**(1/j))
print("The production rate of a well with an intial production rate of 100 barrels/day, an initial decline rate of 2 barrels/day, and a hyperbolic constant of 0.8 is",l)
print("")

#Mohr-Coulomb failure criterion
# (normal stress * tangent of angle of internal friction) + cohesion
m = 20 #normal stress (lbf/in^2)
o = radians(35) #angle of internal friction
n = tan(o) #the slope of the failure envelope
p = 2 #cohesion (lbf/in^2)
q = (m*n)+p
print("The Mohr-Coulomb Failure Criterion when normal stress of 20lbf/in^2 is applied to a material with cohesion 2lbf/in^2 and angle of internal friction of 35 degrees is",q)