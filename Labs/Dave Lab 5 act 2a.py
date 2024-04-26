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

print('The subject cubic polynomial is: Ax^3 + Bx^2 + Cx + D.')

print('You will be asked to enter values for all four coefficients.')

print('The program will interate and inform you of the resulting first order differential equation.')

A = float(input('Please enter a value for the coefficient A:'))
B = float(input('Please enter a value for the coefficient B:'))
C = float(input('Please enter a value for the coefficiant C:'))
D = float(input('Please enter a value for the coefficient D:'))

print('You have identified', A,'x^3 +', B,'x^2 +',C,'x +',D,'as the subject polynomial.')

#Now we need to deterimine the first order differential equation.  The following uses the power rule.

A_d = A*3
B_d = B*2
C_d = C*1
D_d = D*0

print('The first order differential equation is:', A_d,'x^2 +', B_d,'x +',C_d)

x = float(input('Please provide a value for x in order to evaluate the derivative at that point:'))

print('The derivative dy/dx equals:', A_d*x**2 + B_d*x + C_d) 



