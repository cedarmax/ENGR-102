# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell, David Simpson, and Muhammad Amer
# Section:        537
# Assignment:     Lab 4 Activity 3
# Date:           27 September 2019

#PART A: INPUTTING BOOLEAN VALUES FROM THE KEYBOARD

UserInput = (input("Please enter 'True', 'T', or 't' for True; or 'False', 'F', or 'f' for False: "))

if UserInput == "True" or UserInput == "T" or UserInput == "t":
	print("Value is true")
elif UserInput == "False" or UserInput == "F" or UserInput == "f":
	print("Value is false")
else:
	print("Invalid statement")

#PART B: EVALUATING BOOLEANS

a = input("Please enter 'True', 'T', or 't' for 'True'; or 'False', 'F', or 'f' for 'False' for A: ")
b = input("Please enter 'True', 'T', or 't' for 'True'; or 'False', 'F', or 'f' for 'False' for B: ")
c = input("Please enter 'True', 'T', or 't' for 'True'; or 'False', 'F', or 'f' for 'False' for C: ")

if a == "True" or a == "T" or a == "t":
	a_boolean = bool(1)
elif a == "False" or a == "F" or a == "f":
	a_boolean = bool(0)
else:
	print("Invalid boolean value")
	
if b == "True" or b == "T" or b == "t":
	b_boolean = bool(1)
elif b == "False" or b == "F" or b == "f":
	b_boolean = bool(0)
else:
	print("Invalid boolean value")
	
if c == "True" or c == "T" or c == "t":
	c_boolean = bool(1)
elif c == "False" or c == "F" or c == "f":
	c_boolean = bool(0)
else:
	print("Invalid boolean value")
	
print("A and B and C are", a_boolean and b_boolean and c_boolean)
print("A or B or C are", a_boolean or b_boolean or c_boolean)

#PART C: WRITING BOOLEAN EXPRESSIONS

#1. Didn't use a and b because those were used earlier.

d = bool(0)
e = bool(0)

print(d != e)

#2. Used x, y, and z instead of a, b, and c because I had used those above.

x = bool(0)
y = bool(1)
z = bool(1)

print((x and y and z) or not ((x and y) or (x and z) or (y and z) or (not x and not y and not z)))




