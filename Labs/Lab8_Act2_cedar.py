# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell, David Simpson, Muhammad Amer
# Section:        537
# Assignment:     Lab 8
# Date:           25 October 2019

#M = (N * sigma(x*y) – sigma(x) * sigma(y))/(N * sigma(x**2) – sigma(x**2))

x_list = [1,3,4,5] #For testing purposes, in the final version the list will be user provided
y_list = [3,2,1,4]
product = 0
x_squared = 0

N = len(x_list)
x_sum = sum(x_list)
y_sum = sum(y_list)

for i, j in enumerate(x_list):
	product += j * y_list[i]

numerator = N * product - x_sum * y_sum

for i in x_list:
	x_squared += i**2

denominator = N * x_squared - x_sum**2

m = numerator / denominator #Slope