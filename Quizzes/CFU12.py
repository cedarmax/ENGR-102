 # *************************************************************************************

from math import * #importing all math functions

r_user = float(input("Please enter the r value of your polar coordinate: ")) #This retrieves the values from the user:

theta_user = float(input("Please enter the theta value of your polar coordinate: "))

def polarconvert(r, theta): #defining the function before it needs to be called

﻿'''This function converts polar coordinates to Cartesian coordinates'''

x = r * cos(theta)

y = r * sin(theta)

print("The Cartesian coordinates are: (", x, ",", y, ")") #function prints the result instead of returning

polarconvert(r_user, theta_user) #function is called and Cartesian coordinates will be output

# *************************************************************************************