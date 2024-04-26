UserInput = ""
initial = []
feet = []
inches = []
new2 = []
centimeters = []

print("Enter in a height as a number of feet and inches separated by a space.")
print("For example, 5'9\" would be entered as: 5 9")
print("When complete, enter \"0 0\"")

while UserInput != "0 0":
	UserInput = input("Enter Height: ")
	initial.append(UserInput)
print(initial)

for i in initial:
	new = i.split()
	new2.append(new)
	
print("new2 list is",new2)

# for i,j in enumerate(new2):
	# feet.append(i)

# for i in new2[1]:
	# inches.append(i)

for i,j in enumerate(new2):
	for i in new2[i:0]:
		feet.append(j)
	for i in new2[i:1]:
		inches.append(j)
# print(feet)
# print(inches)

#This doesn't work.  I couldn't figure out how to properly reference lists within lists and split them.

# for i in feet:
	# inches.append(i * 12)
# for i in inches:
	# centimeters.append(i * 2.54)

print("The height of every individual in cm's is: ", centimeters)

