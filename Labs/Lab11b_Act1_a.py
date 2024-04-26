# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 11b Activity 1a
# Date:           15 November 2019

from math import pi, acos, sqrt
#inputs from the user:
print("This program takes the dimensions of a box and the radius of a cylinder drilled in it and returns the remaining volume of the box.")
units = input("Which units will you be using? (Please use the same units for all measurements): ")
user_length = float(input("Please enter the length: "))
user_width = float(input("Please enter the width: ")) #all measurements are the same units, assumedly
user_height = float(input("Please enter the height: "))
user_radius = float(input("Please enter the radius: "))

def remaining(length, width, height, radius):
	'''This function computes the difference in volume after a cylinder is drilled into a box'''
	box_volume = length * width * height
	cylinder_volume = pi * radius**2 * height
	if radius > min(length/2, width/2):
		if (radius > (width / 2)) and not (radius > (length / 2)):
			#WIDTH-WISE HALF MOONS (_ww denotes width-wise)
			#The 'half-moons' are the portions of the cylinder protruding from the box
			a_ww = sqrt((radius**2) - ((width/2)**2)) #A is the portion of the triangle created by drawing the radius to the edge of where the cylinder begins to protrude from the box
			theta_ww = 2 * acos((width / (2 * radius))) #angle measurement of the sector formed
			sector_area_ww = (theta_ww / 2) * radius**2 #area of the entire sector including what is within the box
			triangle_area_ww = (a_ww*2) * (width/2) * .5
			half_moon_area_ww = sector_area_ww - triangle_area_ww 
			half_moon_volume_ww = half_moon_area_ww * height
			remaining_volume = box_volume - (cylinder_volume - (2 * half_moon_volume_ww))
		elif (radius > (length / 2)) and not (radius > (width / 2)):
			#LENGTH-WISE HALF MOONS (_lw denotes length-wise)
			#Length must be calculated separately.  If these lines are run
			#when the condition is not true, math errors occur.
			a_lw = sqrt((radius**2) - ((length/2)**2)) #Again, unknown side of the triangle
			#^^Above is the pythagorean theorem, rearranged.
			theta_lw = 2 * acos((length / (2 * radius)))
			#cos = adjacent / hypotenuse ^^^^
			sector_area_lw = (theta_lw / 2) * radius**2
			#^^^Area of a sector = (theta / 2) * r^2
			triangle_area_lw = (a_lw*2) * (length/2) * .5 #b * h * 1/2
			half_moon_area_lw = sector_area_lw - triangle_area_lw
			half_moon_volume_lw = half_moon_area_lw * height #volume is always just area * height
			remaining_volume = box_volume - (cylinder_volume - (2 * half_moon_volume_lw)) #FINAL
		else: 
			#The code in this 'else' statement is redundant, see the code above for comments
			#The reasons this is redundant is because these lines cannot be run at once
			#if radius does not exceed BOTH length and width (math error)
			#WIDTH-WISE HALF MOONS (_ww denotes width-wise)
			a_ww = sqrt((radius**2) - ((width/2)**2))
			theta_ww = 2 * acos((width / (2 * radius))) #angle measurement of the sector formed
			sector_area_ww = (theta_ww / 2) * radius**2
			triangle_area_ww = (a_ww*2) * (width/2) * .5
			half_moon_area_ww = sector_area_ww - triangle_area_ww
			half_moon_volume_ww = half_moon_area_ww * height
			#LENGTH-WISE HALF MOONS (_lw denotes length-wise)
			a_lw = sqrt((radius**2) - ((length/2)**2))
			theta_lw = 2 * acos((length / (2 * radius)))
			sector_area_lw = (theta_lw / 2) * radius**2
			triangle_area_lw = (a_lw*2) * (length/2) * .5
			half_moon_area_lw = sector_area_lw - triangle_area_lw
			half_moon_volume_lw = half_moon_area_lw * height
			remaining_volume = box_volume - (cylinder_volume - ((2 * half_moon_volume_lw) + (2 * half_moon_volume_ww)))
	else:
		remaining_volume = box_volume - cylinder_volume
	if remaining_volume < 0: #remaining volume can't be negative (no box left!)
		remaining_volume = 0
	return remaining_volume

print("The remaining volume is", remaining(user_length, user_width, user_height, user_radius), units, "cubed.")