# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell, Muhammad Amer, David Simpson
# Section:        537
# Assignment:     Lab 4 Activity 2
# Date:           27 September 2019

from math import *

UserInput = float(input("How many hours were you parked? "))
UserInput2 = ceil(UserInput)
# ^This way, the number of hours is always rounded up.

#Hours and days must be calculated separately for accurate calculation of multi-day stays.
days = UserInput2 // 24
hours = (abs(UserInput2)) % 24 #absolute value since negative time does not actually exist.
#Since ceil always rounds up, negative days must be calculated separately from positive days.
#Negative days were always rounded up instead of down, producing inaccurate calculation.
negativeDays = abs(ceil(UserInput2 / 24)) # absolute value so multiplication produces positive number.

#This assumes that the negative charge is the same plus the $36 lost ticket charge.
#This program accurately reports all of the test values in the lab assignment pdf.
if UserInput2 < 0:
	if hours == 0 and days != 0:
		print("The fee is", (negativeDays * 24) + 36, "dollars.")
	elif 0<= hours <= 2:
		print("The fee is", (negativeDays * 24) + 4 + 36, "dollars.")
	elif 2<= hours <= 4:
		print("The fee is", (negativeDays * 24) + 7 + 36, "dollars.")
	elif 4<= hours <= 21:
		print("The fee is", (negativeDays * 24) + hours + 3 + 36, "dollars.")
	elif 22<= hours <=24:
		print("The fee is", (negativeDays * 24) + 24 + 36, "dollars.")
elif UserInput2 >= 0:
	if hours == 0 and days != 0:
		print("The fee is", (days * 24), "dollars.")
	elif 0<= hours <= 2:
		print("The fee is", (days * 24) + 4, "dollars.")
	elif 2<= hours <= 4:
		print("The fee is", (days * 24) + 7, "dollars.")
	elif 4<= hours <= 21:
		print("The fee is", (days * 24) + hours + 3, "dollars.")
	elif 22<= hours <=24:
		print("The fee is", (days * 24) + 24, "dollars.")
else: #I couldn't get this to work.  I wanted this to print if, say, the user entered a string.  But that actually produces an error in python.
	print("Invalid hour count")
	print("Unknown charge!")