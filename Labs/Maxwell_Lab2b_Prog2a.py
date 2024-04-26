# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar James Maxwell, 828007623
# Section:        537
# Assignment:     Lab 2b Program 2a
# Date:           15 September 2019

time1 = 13
x1 = 1
y1 = 3
z1 = 7

time2 = 84
x2 = 23
y2 = -5
z2 = 10

#Calculating the slope individually for each plane
x_change = x2 - x1
time_change = time2 - time1
xslope = x_change / time_change

y_change = y2 - y1
yslope = y_change / time_change

z_change = z2 - z1
zslope = z_change / time_change

time3 = 50
#Rearranged slope formula for the missing value
x0 = (xslope * time3 + x1)
y0 = (yslope * time3 + y1)
z0 = (zslope * time3 + z1)

print("time of interest =", time3, "seconds")
print("x0 =", x0 ,"m")
print("y0 =", y0 ,"m")
print("z0 =", z0 ,"m")
