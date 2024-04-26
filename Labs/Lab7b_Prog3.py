# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 7b Program 3
# Date:           18 October 2019

#Part A
#sorting the list

numbers = [3,4,9,5,7,7,5,2,8,5,5,3,1,9,2]

numbers.sort()

print("The sorted list is", numbers)

#finding the median

length = len(numbers)
index = (length - 1) // 2

if (length % 2):
	print("The median is", numbers[index])
else:
	print("The median is", (numbers[index] + numbers[index + 1])/2.0)

#Part B

numbers = [3,4,9,5,7,7,5,2,8,5,5,3,1,9,2]

newNumbers = sorted(numbers)
x=1000
for i in numbers[:]:
	newNumbers.append(min(numbers))
	numbers.remove(min(numbers))
print("The new list is:", newNumbers)
print("The original list is now:", numbers)

#Now to create a new list ordered from max to min

numbers2 = [3,4,9,5,7,7,5,2,8,5,5,3,1,9,2]

newNumbers2 = []

for i in numbers2[:]:
	newNumbers2.append(max(numbers2))
	numbers2.remove(max(numbers2))
print("The list [3, 4, 9, 5, 7, 7, 5, 2, 8, 5, 5, 3, 1, 9, 2] sorted from maximum to minimum is", newNumbers2)

if (length % 2):
	print("The median is", newNumbers2[index])
else:
	print("The median is", (newNumbers2[index] + newNumbers2[index + 1])/2.0)