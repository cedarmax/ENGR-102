# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell, David Simpson, Mohammed Amer
# Section:        537
# Assignment:     Lab 7 Activity 1
# Date:           18 October 2019

# This is the request for input of the stock price.

stock_prices = input('Please input three stock prices with a space between them:')

#The intructions require that the input is provided on one string.  The following built-in member funtion
#split it onto spearate strings for consideration of the for loop that follows.

stocks = stock_prices.split()

#The following converts the separate string values into floats.

for i in range (len(stocks)):
    stocks[i] = float(stocks[i])
    
#The following results in the instructed print output with "$" to the left and the decimal two spaces fron the right.

for price in stocks:
    
    print('$''%9.2f' %price)

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