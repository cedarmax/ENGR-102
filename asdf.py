# dictionary = {'Apple':3, 'Pear':5, 'Banana':2}
# dictionary[4] = 'Orange'
#print(dictionary[3])
# print(dictionary['Apple'])

# import math
# print(dir(math))
# help(math)

# from math import pi

# print(round(pi, 4))
# print("%.100f" % pi)

'''list = [3,4]
print(list * 3)

vector1 = (1, 2, 3)
vector2 = (2, 3, 4)
dotp = vector1 * vector2
print("The dot product is", dotp)'''

import numpy
from matplotlib import pyplot

x = [4,3,7,0]
y = [1,2,3,4]
a = numpy.array([3,2,1])
#try:
#except:


pyplot.plot(x,y, label="C")
pyplot.plot(y,x, label="ZEZ")
pyplot.legend(loc='upper right')
pyplot.title("COck")
pyplot.show()
# import os
# path = 'C:\\Users\\Cedar\\AppData\\Local\\Programs\\Python\\Python37\\Scripts'
# os.environ['PATH'] += ':'+path

# print("Done")

# x = 3
# y = 5

'''print(x != y - 2)
print(x >= 0 and not x < 10)
print(x < 0 and x < 10)
print(x >= 0 and x < 2)
print(x < 0 or y < 5)
print(not x > 0 or x < 10)'''

#Prior Exam Questions

#1.

"""x = int(input())
y = int(input())
z = int(input())
a = int(input())
b = int(input())

if (x == y) or (x == z) or (x == a) or (x == b) or (y == z) or (y == a) or (y == b) or (z == a) or (z == b) or (a == b):
	print("Duplicates")
else:
	print("All Unique")"""

#2.

#3.

# list_words = ["John", "Sue", "Chris"]
# word = list_words.split()
# print(word)

# maxlength = max(list_words)
# longest = len(maxlength)
# print("The longest word", maxlength, "has", longest, "characters.")

#4. 

"""x = float(input("Please enter a float between 1 and -1: "))
y = 0

while y < 7:
	print((1/(1-x)))
	x /= 10
	y += 1
	
y = ((y2-y1)/(x2-x1))*(x-x1)+y1"""

# name = input("Please enter name of the file to be created: ")



# myjournal = open('journal.txt', 'r+')
# contents = myjournal.read()
# print("The contents,", contents)
# num1 = "hello"
# myjournal.write(num1)

# for line in contents:
	# print(line)