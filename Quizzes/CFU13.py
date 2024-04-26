# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar James Maxwell
# Section:        102-537
# Assignment:     CFU 13
# Date:           20 November 2019

#Part 1

def leapyears(start_year, end_year):
	'''This function takes in a date range and returns the number of leap years, start and end inclusive'''
	leap_years_list = []
	for i in range(start_year, end_year + 1):
		if (i % 4 == 0) and ((not (i % 100 == 0)) or (i % 400 == 0)): #divisible by four, but not 100 unless also 400
			leap_years_list.append(i) 
	return leap_years_list

print(leapyears(1980, 2015))

#Part 2

with open ('LeapDates.txt', 'r') as table:
	contents = table.read().split('\n') #Each element in this list contains both years on that particular line
	list_of_lists = []
	for i in contents:
		list_of_lists.append(i.split(',')) #This creates our list of lists, or 2D list
	print(list_of_lists) #This is included so that you can see my 2D list

#Part 3

with open ('LeapYearRanges.txt', 'w') as table:
	for i in list_of_lists:
		#WrittenString is the string to be written to the file
		#The .write() function only accepts 1 argument, so I had to combine all my elements into one string before writing it
		WrittenString = 'for range ['
		WrittenString += i[0] 
		WrittenString += ', '
		WrittenString += i[1]
		WrittenString += ']: '
		WrittenString += str(leapyears(int(i[0]), int(i[1])))
		WrittenString += '\n'
		table.write(WrittenString)