T = open('Temperature.dat', 'w')
T.write("75\n78\n82\n77\n80\n64\n99")
T.close()

#Opening and closing the file to allow for writing and reading (w+ would not work for some reason)

N = open('Temperature.dat', 'r')
temps = N.read().split('\n')
print("The temperatures are:\n", temps)

newFile = open('WeeklyAverages.dat', 'w')
x = 0

for line in temps:
	x += int(line)
avg = x / 7

newFile.write()
newFile.close()

NewNewFile = open('WeeklyAverages.dat', 'r')
average = NewNewFile.read()
print("The average temperature is", average)

