# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 11b Activity 1e
# Date:           14 November 2019

testList = [3,3,4,44,5,52,5,621,6,1346,1634,16,1436]

def ListStats(list):
	'''This function returns the max, min, and mean of a list'''
	maximum = max(list) #Wasn't sure if we could use max() or if we had to do it manually
	minimum = min(list)
	average = sum(list) / len(list)
	return maximum, minimum, average

print("The maximum, minimum, and average of the list respectively are: ", ListStats(testList))