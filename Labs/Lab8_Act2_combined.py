# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
 # Names:          Cedar Maxwell
 #                 Muhammed Amer
 #                 David Simpson
 # Section:        537
 # Assignment:     Lab 8, Activity 2
 # Date:           27 October 2019
#User inputs for x y coordinates:
#[Dave start]
print('You will be asked to provide up to 10 pairs of x, y coordinates, with spaces separating the numbers.')
print('For example, for the two pairs of x,y coordiantes 3,4 and 5,6 you would enter: 3 4 5 6')

user_input = (input('Please provide up to 10 x,y coordinates:'))

values = user_input.split()

for i in range (len(values)):
    values[i] = float(values[i])

nums = []

for value in values:
    nums.append(value)

#This is just a check to make sure the entered numbers got into the nums list after conversion to float.

print(nums) #This print is a check to make sure the input values came through accurately in floats.


#This is just a double check index to values.
for index in range (len(nums)):
    value = nums[index]
    print(index, value) #Consider removing this print statement
    
#The following is intended to build two separate xy lists for use in the line fit problem that follows.
x_list = []
y_list = []

#This separates the combined xy list into separate x and y lists.
x_list = nums[::2]
y_list = nums[1::2]

print(x_list)  #This is provided in order to ensure that the x_list and y_list values were correctly captured.
print(y_list)

#Consider hiding printing out the x_list and y_list, especially accompanied by no text

#[Cedar Start)

product = 0
x_squared = 0

N = len(x_list)
x_sum = sum(x_list)
y_sum = sum(y_list)

for i, j in enumerate(x_list):
    product += j * y_list[i]

numerator = N * product - x_sum * y_sum

for i in x_list:
    x_squared += i**2

denominator = N * x_squared - x_sum**2

m = numerator / denominator #Slope

print("The slope is", m)

#Muhammad's part recreated by Cedar

b = (y_sum - m * x_sum) / N

x = int(input("Please enter an x-value, and the corresponding y-value will be calculated: "))
#y = mx+ b
y = m * x + b

print("The corresponding y-value is:", y)