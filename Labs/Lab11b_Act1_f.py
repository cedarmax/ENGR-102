# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 11b Activity 1f
# Date:           14 November 2019

test_times = [1, 3, 5, 7, 9] #possibly user inputted in the future
test_distances = [40, 55, 80, 120, 190]

def avg_velo(times, distances):
	'''This function calculates the average velocity between each consecutive time and distance value'''
	delta_distance = [] #empty lists to be appended to
	delta_time = []
	average_velocity = []
	for i,j in enumerate(distances): #using enumerate function to retain index AND value of list for that index
		#enumerate allows me to reference two lists at once
		if i+1 >= len(distances): #this is to prevent the index from exceeding the length of the list
			continue
		delta_distance.append(distances[i+1] - j)
	for i,j in enumerate(times):
		if i+1 >= len(times):
			continue
		delta_time.append(times[i+1] - j)
	for i,j in enumerate(delta_distance):
		average_velocity.append(j / delta_time[i])
	return average_velocity
	
print("The average velocities between each time/distance measurement are:", avg_velo(test_times, test_distances))