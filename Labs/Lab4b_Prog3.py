# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 4b Program 3
# Date:           27 September 2019

print("This program reports the production of a machine on the day specified by the user.")
day = float(input("Please enter the number of the day (1-100) you would like to know production for: "))

if 1 <= day < 11:
	widget = 0
	widget = day * 10
	print("The production on day", day, "is", widget, "widgets a day.")
elif 11 <= day <= 60:
	widget = 100
	widget += (day - 10)*40
	print("The production on day", day, "is", widget, "widgets a day")
elif 60 < day < 100:
	widget = 2100
	widget_day = 99 - day
	total = (widget_day * (widget_day+1))/2
	widget += 780 - total
	print("The production on day", day, "is", widget, "widgets a day.")
elif 100 <= day:
	print("The machine is no longer functioning on this day.")
elif day < 0:
	print("Negative day numbers are not valid.")
else:
	print("Invalid number of days!.")