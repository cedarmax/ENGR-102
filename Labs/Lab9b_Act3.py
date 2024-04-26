# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell
# Section:        537
# Assignment:     Lab 9b Activity 3
# Date:           1 November 2019

AveragesSummed = 0
JulyAveragesSummed = 0
humiddaycount = 0

with open("WeatherDataWindows.csv", 'r') as table:
	contents = table.read().split('\n')
	max = 0
	for line in contents: #Max 'for' loop
		new = line.split(',')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[1] == 'Temp High': #First line is a header
			continue
		elif int(new[1]) > max:
			max = int(new[1])
	for line in contents: #Average 'for' loop
		#Separate for loops because the if statements were confusing all inside one loop
		new = line.split(',')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[2] == 'Temp Avg': #First line is a header
			continue
		AveragesSummed += int(new[2])
	for line in contents: #Loop to calculate max/min Christmas temperatures
		new = line.split(',')
		date = new[0].split('/')
		if date[0] == '12' and date[1] == '25':
			print("On Christmas in the year", date[2], "the maximum temperature was", new[1], "and the minimum temperature was", new[3], "degrees Fahrenheit.")
	for line in contents: #Calculate July average high temp
		new = line.split(',')
		date = new[0].split('/')
		if date[0] == '7' and date[2] == '2015':
			JulyAveragesSummed += int(new[1])
	for line in contents:
		new = line.split(',')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[8] == 'Humidity Avg': #First line is a header
			continue
		elif float(new[8]) >= 90:
			humiddaycount += 1
		
	totalAverage = AveragesSummed / 1095 #Correlates to my second 'for' loop, written here so as not to be altered by the loop.
	
	print("The percentage of days on which the average humidity was above 90% is", (humiddaycount / 1095) * 100, "percent")
	print("The average daily high temperature in July 2015 is", JulyAveragesSummed / 31, "degrees Fahrenheit.")
	print("The average daily temperature is", totalAverage, "degrees Fahrenheit.")
	print("The maximum daily temperature is", max, "degrees Fahrenheit.")