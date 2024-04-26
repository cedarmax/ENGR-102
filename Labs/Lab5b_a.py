# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 5b Activity 3c
# Date:           4 October 2019

#The Collatz Conjecture

print("This program takes any given integer and applies the Collatz Conjecture.")
n = int(input("Please enter a number: "))

x = 0

if n < 0:
	print("Negative numbers are not permitted.")
while n > 1:
	if n % 2 == 0:
		n /= 2
		x += 1
	else:
		n *= 3
		n += 1
		x += 1
	print(n)
print("It took", x, "steps to reach 1.")