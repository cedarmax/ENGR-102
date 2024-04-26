# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Cedar Maxwell
# Section:        537
# Assignment:     Lab 11b Activity 1b
# Date:           15 November 2019

facilities = ["Dallas", "FW", "Austin"] #made up stuffs
annual_cost = [100, 50, 95]
revenue = [1000, 500, 240]
net = [] #pre-created for appending

def WorstPerformer(facilities, annual_cost, revenue, net):
	'''This function determines which facility is least profitable'''
	for i,j in enumerate(annual_cost):
		#Enumerate() allows me to reference two lists at once with the same index
		net.append(revenue[i]- j)
	return facilities[net.index(min(net))], min(net)

print("The least profitable facility followed by its net profitability is:", WorstPerformer(facilities, annual_cost, revenue, net))