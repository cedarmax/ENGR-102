# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar James Maxwell
# Section:        537
# Assignment:     Lab 1b Program 2
# Date:           28 August 2019
from math import*

#Each new value is printed out on its own line.
#Function 1, f(x)=sinx/x.  Each successive value for x is 1/10th the previous size.
print("This shows the evaluation of sin(x)/x evaluated close to x=1.")
print("For these first two equations, x will increase by one negative power of ten each time.")
print("My guess is ~pi/6 for the first result, after which the results will be slightly larger.")
print("")
x=1
print((sin(x))/x)
print((sin(x-.9))/(x-.9))
print((sin(x-.99))/(x-.99))
print((sin(x-.999))/(x-.999))
print((sin(x-.9999))/(x-.9999))
print((sin(x-.99999))/(x-.99999))
print((sin(x-.999999))/(x-.999999))
print((sin(x-.9999999))/(x-.9999999))
print("")

#Function 2, g(x)=1-cosx/x^2.  Each successive value for x is 1/10th the previous size.
print("Next, the function (1-cosx)/x^2 will be demonstrated.  I expect the results to also have little difference between each other after the first calculation, which should also be near pi/6.")
print("")

print((1-cos(x))/(x**2))
print((1-cos(x-.9))/((x-.9)**2))
print((1-cos(x-.99))/((x-.99)**2))
print((1-cos(x-.999))/((x-.999)**2))
print((1-cos(x-.9999))/((x-.9999)**2))
print((1-cos(x-.99999))/((x-.99999)**2))
print((1-cos(x-.999999))/((x-.999999)**2))
print((1-cos(x-.9999999))/((x-.9999999)**2))
print("")

#Function 3, h(x)=(1+1/x)^x.  Each successive value for x is 10 times the previous size.
print("Finally, the function h(x)=(1+(1/x)^x will be evaluated at x=1 through 10^7.  The first result should be 2.  I expect the results after will be increasingly smaller.")
print("For this function, x will increase by one power of ten each time")
print("")

print((1+(1/(x))**(x)))
print((1+(1/(x+9))**(x+9)))
print((1+(1/(x+99))**(x+99)))
print((1+(1/(x+999))**(x+999)))
print((1+(1/(x+9999))**(x+9999)))
print((1+(1/(x+99999))**(x+99999)))
print((1+(1/(x+999999))**(x+999999)))
print((1+(1/(x+9999999))**(x+9999999)))