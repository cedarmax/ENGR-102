# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 3b Activity 4 Program 1b
# Date:           20 September 2019

print("This program calculates the kinetic energy of an object given the mass and velocity.")

#Kinetic Energy, 1/2*a*b^2
mass = float(input("What is the mass in kilograms? "))
velocity = float(input("What is the velocity in meters per second? "))
kineticEnergy = .5*mass*(velocity**2)
print("Kinetic energy in joules is defined by the equation 1/2mv^2.  If the mass of an object traveling at", velocity, "m/s is", mass, "kg, then the kinetic energy is", '%.4f'%(kineticEnergy), "joules.");
print("")
