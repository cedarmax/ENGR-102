# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 7, Activity 1, Part 3 
# Date:           18 October 2019

#We were told to reference Zybook Challenge Activity in order to create a
#printout of the hard-coded list with a seperator symbol with extra spaces surrounding
#the sepeerator.

#These are the hard-coded temperatures.

myTemps = [75, 87, 95, 102, 76]

#This is the range for the loop.

myTemps_len = len(myTemps)

#This is the loop which goes across and prints the list sequentially in accordance with
#what was entered.

for i in range (myTemps_len):
    print(myTemps[i], end=' ')
    
    if i < myTemps_len - 1:
        print(' -> ', end=' ')
print()