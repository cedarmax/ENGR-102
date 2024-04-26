# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:         Cedar Maxwell
# Section:      537
# Assignment:   Lab 2
# Date:         15 September 2019
from math import *
#Part 1 - Write program for that determines where the car is on the track for any time between 30 and 45 seconds.
#Given: First and second measurements, 30 secs at 50 m and 45 secs at 615 m.

y1 = 50
y2 = 615
x1 = 30
x2 = 45
position_change = y2 - y1
time_change = x2 - x1
slope = position_change / time_change
time = 30
print('The slope is:', slope, 'm/sec')
print('The time is:', time, 'seconds')
print('Position v. Time is:', (slope *(time-30) + y1))
time2 = 37
print('The position at 37 seconds is', (slope *(time2-30) + y1))

#Part 2 - Circular Track
#Circumference = pi2r
r = 500 #meters
circumference = 2*pi*r
time3 = 1200 #seconds, converted from minutes
distance = (slope *(time3-30) + y1)
CurrentLapProgress = distance % circumference
print('The position at', time3, 'seconds on a circular track is', CurrentLapProgress)
