# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 5b Activity 3b
# Date:           4 October 2019

print("This program finds the sum of all integers from 0 to the number entered and the product of all integers from 1 to the number entered.")
n = int(input("Please enter a positive integer: "))

#Sum:

x = 1

for i in range(x):
	s = (n*(n+1)) / 2
	print("For loop: the sum of all numbers between 0 and", n, "is", s)
while x == 1:
	s = (n*(n+1)) / 2
	print("While loop: the sum of all numbers between 0 and", n, "is", s)
	x += 1
	
#Product:

ans = 1
i = 1
z = 1

for i in range(1, n +1):
	ans *= i
print("For loop: The factorial of", n, "is", ans)

i = 1

while i <= n:
	z *= i
	i += 1
print("While loop: The factorial of", n, "is", z)

