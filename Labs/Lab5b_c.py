# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 5b Activity 3c
# Date:           4 October 2019

print("This program finds and counts the prime numbers between 2 and 100.")

y = 0

for num in range(2,101):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				print(num, "is not a prime number.")
				break
		else:
			print(num, "is a prime number.")
			y += 1
print("There are", y, "prime numbers between 2 and 100.")