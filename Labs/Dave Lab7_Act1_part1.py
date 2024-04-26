# By submitting this assignment, all team members agree to the following:
 #  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
 # Names:          Cedar Maxwell
 #                 Muhammad Amer
 #                 David Simpson
 # Section:        537
 # Assignment:     Lab 7, Activity 1, Part 1
 # Date:           20 October 2019

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

