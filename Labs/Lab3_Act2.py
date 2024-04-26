# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Muhammad Amer
#                 Cedar Maxwell
#                 David Simpson
# Section:        537
# Assignment:     Lab 3 Activity 2
# Date:           20 September 2019

#First asking for first member Name and Birthday
Name_person_1 = str(input("First Person, What's your name:"))
Birthday_person_1 = str(input("First Person, When is your birthday:"))
#Asking second member Name and Birthday
Name_person_2 = str(input("Second Person, What is your Name:"))
Birthday_person_2 = str(input("Second person, When is your birthday:"))
#Asking third member name and birthday
Name_person_3 = str(input("Third person, What is your name:"))
Birthday_person_3 = str(input("Third person, What is your birthday:"))
#Asking fourth member name and birthday
Name_person_4 = str(input("Fourth person, What is your Name:"))
Birthday_person_4 = str(input("Fourth person, When is your birthday:"))
#Printing Every member name and birthday. Have r.just(20) to make space between name and birthday
Name="Name"
Birthday = "Birthday"
print("%-20s     %s"%(Name,Birthday))
print("%-20s     %s" %(Name_person_1,Birthday_person_1))
print("%-20s     %s" %(Name_person_2,Birthday_person_2))
print("%-20s     %s"%(Name_person_3,Birthday_person_3))
print("%-20s     %s"%(Name_person_4,Birthday_person_4))
