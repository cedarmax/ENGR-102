# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 3b Activity 4 Program 2
# Date:           20 September 2019

from math import *

# V = 5i + 6j + 7k
# <5,6,7>

#Asking the user for values:
x0 = float(input("Please enter the x coordinate of the observer's position: "))
y0 = float(input("Please enter the y coordinate of the observer's position: "))
z0 = float(input("Please enter the z coordinate of the observer's position: "))
x1 = float(input("Please enter the x coordinate of the first observed point: "))
y1 = float(input("Please enter the y coordinate of the first observed point: "))
z1 = float(input("Please enter the z coordinate of the first observed point: "))
x2 = float(input("Please enter the x coordinate of the second observed point: "))
y2 = float(input("Please enter the y coordinate of the second observed point: "))
z2 = float(input("Please enter the z coordinate of the second observed point: "))

#Creating vectors
#v1 = (x1 - x0, y1 - y0, z1 - z0)
#v2 = (x2 - x0, y2 - y0, z2 - z0)
v1x = x1 - x0
v1y = y1 - y0
v1z = z1 - z0
v2x = x2 - x0
v2y = y2 - y0
v2z = z2 - z0
#print(v1)
#print(v2)
#print((v1x, v1y, v1z))
#print((v2x, v2y, v2z))

#Dot product
dot_product = v1x * v2x + v1y * v2y + v1z * v2z

#print("Dot product is ", dot_product)

#Magnitudes: square root of each vector value squared

m1 = sqrt(((v1x)**2)+((v1y)**2)+((v1z)**2))
m2 = sqrt(((v2x)**2)+((v2y)**2)+((v2z)**2))
#print("Magnitude 1 is", m1)
#print("Magnitude 2 is", m2)

#Calculation of the angle

rad = acos(dot_product / (m1 * m2))
deg = degrees(rad)

#Output

print("Observer location is x=", x0, "y=", y0, "z=", z0)
print("Point 1 location is x=", x1, "y=", y1, "z=", z1)
print("Point 2 location is x=", x2, "y=", y2, "z=", z2)
print("The angle between the points is", '%.2f'%(deg), "degrees.")