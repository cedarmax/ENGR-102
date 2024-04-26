coord = [1,2]
new_coord = []
dict_add = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}
x = 0
y = 0
a = 0
for i in range(4):
	x,y = dict_add[i]
	newcoord = coord[0] + x,coord[1] + y
	print(newcoord)

