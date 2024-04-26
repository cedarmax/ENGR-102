# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        ENGR 102-537
# Assignment:     Lab 10b Activity 2
# Date:           8 November 2019

import numpy as np
import matplotlib.pyplot as plt

#Declaration of values:
AveragesSummed = 0
JulyAveragesSummed = 0
humiddaycount = 0
Average_list = []
day_list = []
day_count = 0
pressure_day_count = 0
pressure_day_list = []
Pressure_list = []
Precipitation_list = []
dew_point_avg_list = []
FIGURE1 = 1
FIGURE2 = 2	
FIGURE3 = 3
FIGURE4 = 4

with open("WeatherDataWindows.csv", 'r') as table:
	contents = table.read().split('\n')	
	for line in contents: #Pressure 'for' loop
		new = line.split(',')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[11] == 'Pressure Avg': #First line is a header
			continue
		Pressure_list.append(float(new[11]))
		pressure_day_count += 1
		pressure_day_list.append(pressure_day_count)
	for line in contents: #Average 'for' loop
		#Separate for loops because the if statements were confusing all inside one loop
		new = line.split(',')
		date = new[0].split('/')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[2] == 'Temp Avg': #First line is a header
			continue
		Average_list.append(int(new[2]))
		day_count += 1
		day_list.append(day_count) #Couldn't get it to plot the correct date, so it just plots the number of days since beginning
	for line in contents:
		new = line.split(',')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[13] == 'Precipitation (in.)': #First line is a header
			continue
		Precipitation_list.append(float(new[13]))
	for line in contents:
		new = line.split(',')
		if new == ['']: #Last line is always '' due to the \n character on each line
			continue
		elif new[5] == 'Dew Point Avg': #First line is a header
			continue
		dew_point_avg_list.append(float(new[6]))
figure = plt.figure(FIGURE1)
left_axis = figure.add_subplot(1,1,1)
right_axis = left_axis.twinx()
left_axis.set_xlabel("Number of days")
left_axis.set_ylabel("Average Pressure")
left_axis.plot(pressure_day_list, Pressure_list, 'r', label="Average Pressure")		
right_axis.set_ylabel("Average Temperature")
right_axis.plot(day_list, Average_list, 'g', label="Average Temperature")
left_axis.legend(shadow=True, loc='upper left')
right_axis.legend(shadow=True, loc='upper right')

figure2 = plt.figure(FIGURE2)
left_axis2 = figure2.add_subplot(1,1,1)
plt.hist(Precipitation_list)
left_axis2.set_xlabel("Precipitation (in.)")
left_axis2.set_ylabel("Days with this amount")

figure3 = plt.figure(FIGURE3)
left_axis3 = figure3.add_subplot(1,1,1)
plt.scatter(Average_list, dew_point_avg_list)
left_axis3.set_xlabel("Average Temperature")
left_axis3.set_ylabel("Average Dew Point")

figure4 = plt.figure(FIGURE4)

plt.show()