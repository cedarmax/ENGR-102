"""
# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 		Erwin Luevano
#               Cedar Maxwell
#               Alex Torres
#               Muhammad Amer 
# Section:		ENGR 102-537
# Assignment:	Game project
# Date:		    01 12 2019

"""
import random as r
import numpy as np

###############################################################################################################

def comp_play():
	dict_directions = {1:'y' ,2:'n'}
	coord = np.array([r.randrange(1,11),r.randrange(1,11)]) 
	direction = dict_directions[r.randint(1,2)]
	return coord,direction


###############################################################################################################
def coord_1():
	#playing_dict = {'pvp','cvp','cvc'}
	coordinate = np.array(input('Enter the row and column Ex:(1,2): ').split(','),dtype = int)
	vertical = input('Enter yes if the ship will extend down and no if it will \n extend to the right. Enter:(y or n): ')
	return coordinate, vertical
# need to see what functions are connected and create user input and computer input
###############################################################################################################

def who_play(whos,num):
	if whos == 'pvp':
		coordinate,vertical = coord_1()
		return coordinate, vertical
	elif whos == 'cvp':
		if num %2 ==1:
			coordinate,vertical = coord_1()
			return coordinate,vertical
		else:
			coordinate, vertical = comp_play()
			return coordinate, vertical
	else:
		coordinate,vertical = comp_play()
		return coordinate, vertical

###############################################################################################################

def board(num):
	if num % 2 == 1:
		player, oppos, name = player_1, opponents_2, 'player 1'
	else:
		player, oppos, name = player_2, opponents_1, 'player 2'
	print('Your attack board')
	for i in oppos:
		print(*i,sep='  ')
	print(name)
	for i in player:
		print(*i,sep= '  ')	


###############################################################################################################
def end(player):
	"""
	
	param: player ~ place the graph of opponent
	
	Checks to see if player has won the match
	
	"""
	a = 0 # counts pieces left
	# Loops through board checking if their are still pieces of opponents ship
	for i in player: #cbdsp
		for t in i:
			if t == 'C':
				a += 1
			elif t == 'B':
				a += 1
			elif t == 'D':
				a += 1
			elif t == 'S':
				a += 1
			elif t == 'P':
				a += 1	
	if a == 0:
			
			print('you won the game!!!')
			return True
	return False
###############################################################################################################		
def moves(num,coord):  
	"""
	
	param: num ~ number of game loop
	param: coord~ coordinate of attack
	
	Will attack opponents board and if players move is a hit will leave a 'X' and if a miss 'O'
	After each players turn will show players board and attack board to see if they hit their opponent and 
		how many times player has been hit 
	
	"""
	
	if coord[0] == 0 or coord[1] == 0:
		return False
	# Resets/creates variables
	player = None
	oppos = None
	if num %2==1: # if player 1 turn will use their variables
		player, oppos= player_2, opponents_2 # player 2 variable
	else: # if player 2 turn will use player two variables
		player, oppos= player_1, opponents_1 # player 2 vairable
	# checks if ship is there and if position has not been hit yet and then marks area as hit/miss with 'X' and 'O' in coordinate of attack
	if player[coord[0]][coord[1]] != '.' and player[coord[0]][coord[1]]!= 'O' and player[coord[0]][coord[1]] != 'X': 
		oppos[coord[0]][coord[1]] = 'X' 
		player[coord[0]][coord[1]] = 'X'
		# prints graph after attacks
		board(num)
		NextMove(coord[0], coord[1])
	elif player[coord[0]][coord[1]] == '.' and player[coord[0]][coord[1]] != 'O' and player[coord[0]][coord[1]] != 'X':
		player[coord[0]][coord[1]] = 'O'
		oppos[coord[0]][coord[1]] = 'O'
		# prints graph after attacks
		board(num)
	# if the spot has been hit then user is able to enter coordinates till they are accepted
	else:
		return False

def NextMove(coord,num):
	new_coord = []
	dict_add = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}
	x = 0
	y = 0
	if (whos == 'cvp' and num %2 == 0 ) or whos == 'cvc':
	for i in range(4):
		while move(num, new_coord) == False:
			newcoord = coord[0] + x,coord[1] + y
			move(
		
	
	return True
###############################################################################################################
def correct_move(num,coord,whos): # makes sure move is allowed 
	l = None
	l = moves(num,coord)   
	# loops until acceptable attack is entered
	while l == False:
		print('You already hit there! Look at your hit sheet and choose another area.')
		print('Enter a coordinate for attack.')
		coord = who_play(whos,num)[0]
		l = moves(num,coord)
###############################################################################################################
###### Cedars placement	
		"""
		Will need to do checks in another function 
		
		"""

def set_tile(board,location,char):
	board[location[0]][location[1]] = char

def place_ship(board,location_origin,length,vertical):
    #location: tuple of coordinates of top of ship
    #length: int to represent length of ship
    #vertical: bool is true if ship is vertical
    #place_ship returns False if placement is invalid

	#place_ship will place partial ships if they leave the board boundaries
    label = {5:[5,'c'],4:[4,'B'],3:[3,'S'],2:[2,'P']} # 3 and 3
    size,ship = label[length]
    x = 0
    y = 0

    location = location_origin
    for i in range(size):
        location = (location_origin[0]+x,location_origin[1]+y)
        set_tile(board,location,ship)
        if vertical == 'Y' or vertical == 'y':
            x += 1
        else:
            y += 1
		


		
###############################################################################################################	
#def rules(player, coordinate, direction, n_range):
def rules_c(player,coordinate,lent,vert):

    dict_tr = {'Y','y','N','n'}
    if vert not in dict_tr:
        print('wasnt in dict')
        return False
    if player[coordinate[0]][coordinate[1]] != '.':
        print('first coord already something there')
        return False
    x = 0
    y = 0
    if vert == 'y' or vert == 'Y':
        if coordinate[0] + length <= 10:
            for i in range(length):
                if player[coordinate[0]+x][coordinate[1]] != '.':
                    print('next space wasnt an empty space for coord[0] +x')
                    return False
                x += 1
        else: 
            print('was out of range coord[0]+length')
            return False
    else:
        if coordinate[1] + length <= 10:
            for i in range(length):
                if player[coordinate[0]][coordinate[1]+y] != '.':
                    print('coord[1] + y')
                    return False
                y += 1
        else: 
            print('was out of range for coord[1]+ legnth')
            return False 
    return True
###############################################################################################################
# placement_c(player_2,coordinate,length,vertical)
def placement_c(player,coordinate,lent,vert,whos): # works with erwins idea of code
	var = None
	var = rules_c(player,coordinate,lent,vert)
	while var == False:
		print('You didnt enter a correct placement try again.')
		print('Enter the coordinate for placement of ship')
		coordinate,vert = who_play(whos,num)
		var = rules_c(player,coordinate,lent,vert)
	return coordinate,vert
###############################################################################################################
	
print('BATTLESHIP')
print('Welcome to the game Battleship.')
print('Rules:\n'
	'You will place your ships on the board any way you like without seeing other players board\n'
	'Once you have placed your ships you will be able to attack any where on your players board\n'
	'The game will ask you where you would like to attack and you place a coordinate on the board with your attack\n'
	'If your attack was a hit a X will be placed on your attack board and oppenents ship board\n'
	'If your attack was a miss an O will be placed on where you have missed\n'
	'The board will inform you if your move is acceptable if not it will let you try again.\n'
	'Enjoy the game!')
whos = input('who is playing today(player v.s player :[pvp], computer v.s player:[cvp], computer v.s computer: [cvc]) :')
print('')
for num in range(1,203): # loops through game until someone wins or all spaces have been used 
###############################################################################################################
	if num ==1 : # player 1 board 
		opponents_2 =[['  ','1','2','3','4','5','6','7','8','9','10','c'],
				      ['1 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['2 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['3 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['4 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['5 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['6 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['7 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['8 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['9 ','.','.','.','.','.','.','.','.','.','.'],
			          ['10','.','.','.','.','.','.','.','.','.','.'],
				      ['r']]
		
		player_1 =   [['  ','1','2','3','4','5','6','7','8','9','10','c'],
				      ['1 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['2 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['3 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['4 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['5 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['6 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['7 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['8 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['9 ','.','.','.','.','.','.','.','.','.','.'],
			          ['10','.','.','.','.','.','.','.','.','.','.'],
				      ['r']]
		
		board(num)	
 		# player sets up their board by placing their ships
		length_dict = {0:[5,'Carrier'],1:[4,'Battleship'],2:[3,'Submarine'],3:[3,'Destroyer'],4:[2,'Patrol Boat']}
		for i in range(5):
			vertical = None
			length, name = length_dict[i]
			print('The',name,'takes up',length,'spaces.' )
			print('Enter the coordinates for your ships placement.')
			coordinate,vertical = who_play(whos,num)
			coordinate,vertical = placement_c(player_1,coordinate,length,vertical,whos)
			place_ship(player_1,coordinate,length,vertical)
		# prints players board to see their finished result
			board(num)
		ready = input('Ready to switch? press Enter!')
		print(20*'\n')
		# does not move on until user is ready
		switch = input('If you have swtiched say yes:')
###############################################################################################################
	elif num == 2:
		opponents_1 =[['  ','1','2','3','4','5','6','7','8','9','10','c'],
				      ['1 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['2 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['3 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['4 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['5 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['6 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['7 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['8 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['9 ','.','.','.','.','.','.','.','.','.','.'],
			          ['10','.','.','.','.','.','.','.','.','.','.'],
				      ['r']]
		
		player_2 =   [['  ','1','2','3','4','5','6','7','8','9','10','c'],
				      ['1 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['2 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['3 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['4 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['5 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['6 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['7 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['8 ','.','.','.','.','.','.','.','.','.','.'],
	                  ['9 ','.','.','.','.','.','.','.','.','.','.'],
			          ['10','.','.','.','.','.','.','.','.','.','.'],
				      ['r']]
		
		board(num)
		# thinking of printing out the graph everytime so the person sees where they placed their ships
		# or would it be too much printing????????
		# player sets up their board by placing their ships
		length_dict = {0:[5,'Carrier'],1:[4,'Battleship'],2:[3,'Submarine'],3:[3,'Destroyer'],4:[2,'Patrol Boat']}
		for i in range(5):
			length, name = length_dict[i]
			print('The',name,'takes up',length,'spaces.' )	
			print('Enter the row and column for placement of your ship.')
			coordinate,vertical = who_play(whos,num)
			coordinate,vertical = placement_c(player_1,coordinate,length,vertical,whos)
			place_ship(player_2,coordinate,length,vertical)
			board(num)
		ready = input('Ready to switch? press Enter!')
		print(20*'\n')
		# does not move on until user is ready
		switch = input('If you have swtiched say yes:')
###############################################################################################################	
	# Player 1 turn to attack		
	elif num != 1 and num %2==1:
		board(num)
		print('Player 1 it is your turn!')
		print('Enter the row and column for your attack!')
		coord = who_play(whos,num)[0]
		correct_move(num,coord,whos)
		# checks if player 1 has won
		if end(player_2):
			break
		# allows user to see board after attack
		user = input('See if you hit or missed and press enter for player twos turn!')
		print(20*'\n')
		# does not move on until user is ready
		switch = input('If you have swtiched say yes:')
		
###############################################################################################################		
	# player 2 turn to attack
	elif num !=2 and num %2==0:	
		board(num)
		print('Player 2 it is your turn!')
		print('Enter the row and column for your attack!')
		coord = who_play(whos,num)[0]
		correct_move(num,coord,whos)
		# checks if player 2 has won
		if end(player_1):
			break
		user = input('See if you hit or missed and press enter for player ones turn!')
		print(20*'\n')
		# does not move on until user is ready
		switch = input('If you have swtiched say yes:')