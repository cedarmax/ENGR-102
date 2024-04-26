# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names:          Cedar Maxwell
#                 Muhammed Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 7, Activity 1, Part 2 
# Date:           20 October 2019

#We were instructed to use the code provided in Zybook Figure 7.7.2 and modify it to provide the "minimum odd
#number" in a list of numbers entered by the user.

user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers

nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number

print()  # Print a single newline

for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))

# Determine minimum odd number

min_num = None
for num in nums:
    if (min_num == None) and (num % 2 != 0):
        # First odd number found
        min_num = num
    elif (min_num != None) and (num < min_num ) and (num % 2 !=0):
        # Smaller odd number found
        min_num = num

print('Min odd #:', min_num)
