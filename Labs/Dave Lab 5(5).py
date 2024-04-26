# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
 # Names:          Cedar Maxwell
 #                 Muhammed Amer
 #                 David Simpson
 # Section:        537
 # Assignment:     Lab 5, Activity 1 
 # Date:           4 October 2019

#The team tried the majority of the test cases provided in the examples handed out in the lab.
#Each time the team identified one of the roots in order to enter the bounds [a,b].
#It seemed to work.  
 
print('The subject cubic polynomial is: Ax^3 + Bx^2 + Cx + D.')

print('You will be asked to enter values for all four coefficients.')

print('The program will interate and inform you of an approximation of one of the roots.')

A = float(input('Please enter a value for the coefficient A:'))
B = float(input('Please enter a value for the coefficient B:'))
C = float(input('Please enter a value for the coefficiant C:'))
D = float(input('Please enter a value for the coefficient D:'))

a = float(input('Please provide the lower bound:'))
b = float(input('Please provide the upper bound:'))

#Tested and found correct.
fa = A*a**3 + B*a**2 + C*a + D
fb = A*b**3 + B*b**2 + C*b + D


if (fa * fb) >= 0:
    print ('Bisection method does not apply')

    
while abs (b - a) >= 10e-6: #This is the tolerance.
    p = (a + b)/2
    fp = A*p**3 + B*p**2 + C*p + D
#If both the f(a) and f(p) are either above or below the x-axis, p is still on the same side of the curve
#and p should be the new a in the iteration.  
    if (fp > 0 and fa > 0):
        a = p
    elif (fp < 0 and fa < 0):
        a = p
#If the above is not the case, then p is on the b side of the curve, and should be the new value for b in the iteration.
    else:
        b = p
print('This is the approximate value of the left-most root:', p)