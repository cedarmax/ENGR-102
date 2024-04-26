# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 3b Activity 4 Program 1a
# Date:           20 September 2019

print("This program calculates the voltage given the resistance and current.")

#Ohm's Law, voltage = current * resistance
current = float(input("What is the current in amperes? "))
resistance = float(input("What is the resistance in ohms? "))
voltage = current * resistance
print("If a conductor has a resistance of", resistance, "ohms and a current of", current, "amperes is run across it, the voltage is", '%.4f'%(voltage), "volts.")