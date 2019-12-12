"""
# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names:         Erwin Luevano
#               Cedar Maxwell
#               Alex Torres
#               Muhammad Amer 
# Section:        ENGR 102-537
# Assignment:    Game project
# Date:            01 12 2019
"""
import sys
import random as r
import numpy as np
import winsound as w
from skimage import io
from matplotlib import pyplot as plt

###############################################################################################################

def end(player):
    """
    param:
        player ~ list
    returns:
        False
        True
    Counts the pieces on the board of oponent ship, if there isnt any then will return true to end game
    If user enters end into any of the areas that gives the user the option to, the funciton will end the game
    """
    if player[0] == 'end': # ends game 
        # special effects
        w.PlaySound('outro',w.SND_FILENAME)
        exit_img = io.imread('outro pic.jpg')
        plt.imshow(exit_img)
        sys.exit('You ended the game!') # ends the game
    p = 0 # pieces counter
    # Loops through board checking if their are still pieces of opponents ship
    dict_pieces = {'C','B','S','D','P'} # pieces dictionary
    for i in player: #cbdsp
        for t in i:
            if t in dict_pieces:
                p += 1
    if p == 0:
        print('you won the game!!!')
        w.PlaySound('win_cut',w.SND_FILENAME)
        return True
    return False

###############################################################################################################

def comp_play():
    """
    no parameters
    returns:
        computer generated coordinate and direction
    
    """
    dict_directions = {1:'y' ,2:'n'} # dictionary for computer placement of ship 
    coord = np.array([r.randrange(1,11),r.randrange(1,11)]) # computer generated coordinate 
    direction = dict_directions[r.randint(1,2)] # computer gnereated direction
    return coord,direction 

###############################################################################################################

def coord_1(num):
    """
    param: num ~ int 
        coord_1 ask user to input their coordinate, and if theyre placing their ship it also ask for direction
    returns
        coordinate ~ coordinate can be used for attack or ship placement
        vertical ~ direction of ship placement
    """
    dict_rows = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10} # dictionary for the y axis of board
    vertical = None # vertical is none as place holder if ship placement isnt needed
    # try and except for coordinate entry will stop program if floats and numbers out of range entered
    try:
        print('To end game enter end twice (Ex: end) ')
        coordinate = input('Enter the row and column Ex:(a,2): ').split(',')
        coordinate = np.array([dict_rows[coordinate[0]],coordinate[1]], dtype = int)
        
    except:
        print('For the coordinate you can only enter the letters from a-j and positive whole numbers. Please Try again.')
        print('Enter end  again into the coordinates if you would like to end game (Ex: end)')
        coordinate = input('Enter the row and column Ex:(a,2): ').split(',') 
        if coordinate[0] == 'end':
            end(coordinate) # when player wants to end game
        if coordinate[0] in dict_rows and int(coordinate[1])<=10: # checks to see if everything is correct in entry
            coordinate = np.array([dict_rows[coordinate[0]],coordinate[1]], dtype = int) # creates array for coordinates
        else: # if entry is not correct will loop until it is
            while coordinate[0] not in dict_rows or int(coordinate[1])>10: # loops until everything is correct
                print('For the coordinate you can only enter the letters from a-j and positive whole numbers. Please Try again.')
                print('Enter end  again into the coordinates if you would like to end game (Ex: end)')
                coordinate = input('Enter the row and column Ex:(a,2): ').split(',') 
                if coordinate[0] == 'end': # when player wants to end game
                    end(coordinate)
            coordinate = np.array([dict_rows[coordinate[0]],coordinate[1]], dtype = int) # creates array for coordinate
    if (num == 1) or (num == 2): # runs only if placement of ship is occurring
        vertical = input('Enter yes if the ship will extend down and no if it will \n extend to the right. Enter:(y or n): ')

    return coordinate, vertical

# need to see what functions are connected and create user input and computer input

###############################################################################################################

def who_play(whos,num): 
    """
    
    param:
        whos ~ str
        num ~ int 
    return:
        coordiate and vertical from other user defined funcitons
    uses to find whos playing and lets program decide who enters coordinate
    
    """
    if whos == 'pvp': # if player vs player
        coordinate,vertical = coord_1(num) # calls user entered coordinate function to recieve coordinate and vertical from user
        return coordinate, vertical
    elif whos == 'cvp': # if computer vs player calls user or computer entered function to recieve coordinate and vertical
        if num %2 ==1: # when players turn
            coordinate,vertical = coord_1(num)
            return coordinate,vertical
        else: # when computers turn
            coordinate, vertical = comp_play()
            return coordinate, vertical
    else: # when computer vs computer
        coordinate,vertical = comp_play()
        return coordinate, vertical

###############################################################################################################

def board(num):
    """
    
    param:
        num ~ int
    Prints the players board 
    
    """
    # only prints both boards for player vs player and computer vs player and only prints players board for computer vs player
    if (whos== 'cvc' or whos =='pvp') or (num % 2 == 1 and whos == 'cvp'): 
        if num % 2 == 1: # if player one
            player, oppos, name = player_1, opponents_2, 'player 1'
        else: # if player 2
            player, oppos, name = player_2, opponents_1, 'player 2'
        print('Your attack board')
        for i in oppos:
            print(*i,sep='  ')
        print(name)
        for i in player:
            print(*i,sep= '  ')	
			
###############################################################################################################		

def moves(num,coord,for_next):  
    """
    
    param:
        num ~ int
        coord ~ int array
    returns:
        False
    Recieves coordinate and num to see whos playing. The function checks to see if the move entered has not been used before
    and is on the board. If the move passes all the conditions then the function places and X and O for hit and miss.
    If it is computers move the function saves the hit postions and uses them to find the next best move
    
    """
    # uses global variable for computer smart moves
    global new_coord_1 
    global new_coord_2
    coord_holder = None
    if num %2 ==1: # if player 1
        coord_holder = new_coord_1
    else: # if player 2
        coord_holder = new_coord_2
    
    if coord[0] == 0 or coord[1] == 0: # makes sure move is on board
        return False
    if coord[0] > 10 or coord[1] > 10:
        return False
	# Resets/creates variables
    player = None
    oppos = None
    if num %2==1: # if player 1 turn will use their variables
        player, oppos, coord_holder = player_2, opponents_2, new_coord_1 # player 2 variable
    else: # if player 2 turn will use player two variables
        player, oppos, coord_holder = player_1, opponents_1, new_coord_2 # player 2 vairable
	# checks if ship is there and if position has not been hit yet and then marks area as hit/miss with 'X' and 'O' in coordinate of attack
    if player[coord[0]][coord[1]] != '.' and player[coord[0]][coord[1]]!= 'O' and player[coord[0]][coord[1]] != 'X':
        oppos[coord[0]][coord[1]] = 'X' 
        player[coord[0]][coord[1]] = 'X'
        #w.PlaySound('Blowing up sound fades away', w.SND_FILENAME)        
        coord_holder = [coord[0],coord[1],for_next] # saves hit for computer
        if num %2 ==1: # if player 1
            new_coord_1 = coord_holder
        else: # if player 2
            new_coord_2 = coord_holder
		# prints graph after attacks
        board(num) # prints board
    elif player[coord[0]][coord[1]] == '.' and player[coord[0]][coord[1]] != 'O' and player[coord[0]][coord[1]] != 'X':
        player[coord[0]][coord[1]] = 'O'
        oppos[coord[0]][coord[1]] = 'O'
		# prints graph after attacks
        board(num)
	# if the spot has been hit then user is able to enter coordinates till they are accepted
    else:
        return False
		
###############################################################################################################

def Newmove(num,coord):
    """
    
    param:
        num ~ int
        coord ~ int list
    returns:
        False
    Function checks to see if their was a hit in the move before and checks the areas around the hit
    to try to land another hit. If all the areas around the last hit are taken resets list to no hit and
    generates random computer move. If hit is empty will generate random move 
    
    """
    # global variables for computer genreated move
    global new_coord_1
    global new_coord_2
    coord_holder = None
    if num %2 ==1: # if player 1
        coord_holder = new_coord_1
    else: # if player 2
        coord_holder = new_coord_2
    if coord_holder !=[0,0]: # if the last move was a hit
        dict_next_move = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)} # dictionary for next moves
        newcoord = (coord_holder[0],coord_holder[1]) # new coord created
        # creates variables
        x = 0 
        y = 0
		################################### added len and 3rd parameter to moves function
       
        t_f = moves(num,newcoord,-1) # checks to see if move is valid
        while t_f == False:   # while move around last hit is not valid
            if len(coord_holder) == 3: # if 3 has a smart next move same direction as move before
                if coord_holder[2] >-1: # makes sure correct number is in there
                    x,y = dict_next_move[coord_holder[2]] # changes x and y gives them value
                    newcoord =  (coord_holder[0]+x,coord_holder[1]+y) # creates next coord
                    t_f = moves(num,newcoord,coord_holder[2]) # checks if move is valid
                    if t_f != False: # if is not false will stick with move
                        break
                    if t_f == False: # if false then next move isnt helpful anymore will search around next
                        coord_holder = [coord_holder[0],coord_holder[1]] # takes away next move integer 
            for i in range(4): # loops for next best move
                x,y = dict_next_move[i] # x and y given values
                newcoord =  (coord_holder[0]+x,coord_holder[1]+y) # new coordinate created
                t_f = moves(num,newcoord,i) # checks to see if move is valid
                if t_f != False: # if move was valid breaks outside of loop 
                    break
            if t_f == False: # if all moves around last hit have been used 
                t_f = True # breaks loop
                coord_holder = [0,0] # resets last hit holder
                # applies changes to global hit holder
                if num%2 == 1: # player 1
                    new_coord_1 = coord_holder
                else: # player 2
                    new_coord_2 = coord_holder
                return False # sends back to create random move
    else: # creates random move for when last move was a miss
        t = moves(num,coord,-1) # checks to see if move is valid
        while t == False: # loops until valid move is created
            coord = who_play(whos,num)[0]   # sets new coordinate as first returned value of computer created move
            t = moves(num,coord,-1) # checks if valid move
            
###############################################################################################################

def correct_move(num,coord,whos): 
    """
    
    param:
        num ~ int
        coord ~ list array
        whos ~ str
    Function checks to see if move is valid if not program will loop till user enters a valid move
    
    
    """

    l = None # resets variabke
    if (whos == 'cvp' and num %2 == 0) or whos == 'cvc': # if computer is playing
        l = Newmove(num,coord) # computer move creator
    else: # if player is playing
        l = moves(num,coord,-1)   

	# loops until acceptable attack is entered

    while l == False: # while move is invalid user will able to put a new move until it is valid 
        print('That is in invalid move try again. Check your attack board.')
        print('Enter a coordinate for attack.')
        coord = who_play(whos,num)[0] # coordinated returned from function that creates coordinate
        if (whos == 'cvp' and num %2 == 0) or whos == 'cvc': # if player is playing
            l = Newmove(num,coord)
        else: # if player is playing
            l = moves(num,coord,-1) 

###############################################################################################################

def set_tile(board,location,char):
    """
    
    param:
        board ~ list
        location ~ int list
        char ~ str
    Function places piece of ship
    
    """
    board[location[0]][location[1]] = char # places piece of ship

def place_ship(board,location_origin,size,vertical,label):
    #location: tuple of coordinates of top of ship
    #size: int to represent length of ship
    #vertical: bool is true if ship is vertical
    #place_ship returns False if placement is invalid

	#place_ship will place partial ships if they leave the board boundaries
	
    x = 0
    y = 0

    location = location_origin # variable for location of each piece
	
    for i in range(size): # loops through size of ship to create each ship piece
        location = (location_origin[0]+x,location_origin[1]+y) # adds in direction that piece will be placed
        set_tile(board,location,label) # places piece
        if vertical == 'Y' or vertical == 'y': # what direction the piece will be placed
            x += 1 # adds to the x - axis
        else:
            y += 1 # adds to the y - axis

###############################################################################################################	

#def rules(player, coordinate, direction, n_range):

def rules_c(player,coordinate,lent,vert):
    """
    
    param:
        player ~ list
        coordinate ~ int list
        lent ~ int
        vert ~ str
    returns:
        False
    Program checks postion of ship before it is placed to make sure it is placed correctly if not
    the program will return false. if correct placement is entered user will continue to place ship.
    
    """
    dict_pieces = {'C','B','D','S','P'} # dictionary of pieces
    dict_tr = {'Y','y','N','n'} # dictionary of pieces
    if coordinate[0] >10 or coordinate[1] > 10: # makes sure coordinate is in board
        print('You coordnate was not on the board')
        return False
    if vert not in dict_tr: # makes sure a correct direction was entered
        print('You did not enter a proper direction.')
        return False
    if player[coordinate[0]][coordinate[1]] != '.': # if their is already a piece where user would like to place ship
        print('You were over lapping a ship.')
        return False
    # creates variables
    x = 0
    y = 0
    if vert == 'y' or vert == 'Y': # when the ship extends down
        if coordinate[0] + length-1 <= 10: # if the whole ship will be inside the board
            for i in range(length): # loops through length making sure each piece is not covering another ship
                if player[coordinate[0]+x][coordinate[1]] in dict_pieces or player[coordinate[0]+x][coordinate[1]]!= '.': # where the ship will be placed is not empty
                    print('You were over lapping a ship.')
                    return False
                x += 1
        else: # when ship does not stay in the board
            print('The ship did not stay on the board')
            return False
    else: # if the ship extends toward the right
        if coordinate[1] + length-1 <= 10: # if ship stays in board
            for i in range(length): # loops through length making sure each piece is not covering another ship
                if player[coordinate[0]][coordinate[1]+y] in dict_pieces or player[coordinate[0]][coordinate[1]+y]!= '.': # where the ship will be placed is not empty
                    print('You were over lapping a ship.')
                    return False
                y += 1
        else: # when ship falls off board
            print('The ship did not stay on the board')
            return False 
    return True # returns true if ship placment meets all requirements

###############################################################################################################

def placement_c(player,coordinate,lent,vert,whos): 
    """
    
    param:
        player ~ list
        coordinate ~ int list
        lent ~ int
        vert ~ str
        whos ~ str
    returns:
        coordinate ~ int list
        vert ~ str
    if the coordinate and direction of the ship they are returned if not will ask user to enter both until the coordiante and vert are correct.
    
    """
    var = None # creates variable
    var = rules_c(player,coordinate,lent,vert) # checsk if correct placement entered
    # loops until correct placement is entered
    while var == False:
        print('You didnt enter a correct placement try again.')
        print('Enter the coordinate for placement of ship')
        coordinate,vert = who_play(whos,num) # ask for new coordinates and direction of ship
        var = rules_c(player,coordinate,lent,vert) # checks placemnent
    return coordinate,vert # returns coordinates and direction of ship placement

###############################################################################################################

def main():

    print('BATTLESHIP')

    print('Welcome to the game Battleship.')

    print('Rules:\n'

		'You will place your ships on the board any way you like without seeing other players board\n'

		'Once you have placed your ships you will be able to attack any where on your players board\n'

		'The game will ask you where you would like to attack and you place a coordinate on the board with your attack\n'

		'If your attack was a hit a X will be placed on your attack board and oppenents ship board\n'

		'If your attack was a miss an O will be placed on where you have missed\n'

		'The board will inform you if your move is acceptable if not it will let you try again.\n'
		
		'If you would like to end the game enter end twice to make sure when game ask for coordinates\n'

		'Enjoy the game!')
    #w.PlaySound('intro',w.SND_FILENAME) # plays giving time for user to read rules
    dict_play = {'pvp','cvp','cvc'} # dictionary of valid entries of who is playing
	# ask for correct entry of who will be playing
    global whos
    whos = input('who is playing today(player v.s player :[pvp], computer v.s player:[cvp], computer v.s computer: [cvc]) :')
    while whos not in dict_play:
        whos = input('who is playing today(player v.s player :[pvp], computer v.s player:[cvp], computer v.s computer: [cvc]) :')
    print('')

    length_dict = {0:[5,'Carrier','C'],1:[4,'Battleship','B'],2:[3,'Submarine','S'],3:[3,'Destroyer','D'],4:[2,'Patrol Boat','P']}
    global num
    for num in range(1,203): # loops through game until someone wins 
    
###############################################################################################################
    
        if num ==1 : # player 1 board 
            global opponents_2
            opponents_2 =[['  ','1','2','3','4','5','6','7','8','9','10','c'],
						  ['a ','.','.','.','.','.','.','.','.','.','.'],
						  ['b ','.','.','.','.','.','.','.','.','.','.'],
						  ['c ','.','.','.','.','.','.','.','.','.','.'],
						  ['d ','.','.','.','.','.','.','.','.','.','.'],
						  ['e ','.','.','.','.','.','.','.','.','.','.'],
						  ['f ','.','.','.','.','.','.','.','.','.','.'],
						  ['g ','.','.','.','.','.','.','.','.','.','.'],
						  ['h ','.','.','.','.','.','.','.','.','.','.'],
						  ['i ','.','.','.','.','.','.','.','.','.','.'],
						  ['j ','.','.','.','.','.','.','.','.','.','.'],
						  ['r']]

            global player_1
            player_1 =   [['  ','1','2','3','4','5','6','7','8','9','10','c'],
						  ['a ','.','.','.','.','.','.','.','.','.','.'],
						  ['b ','.','.','.','.','.','.','.','.','.','.'],
						  ['c ','.','.','.','.','.','.','.','.','.','.'],
						  ['d ','.','.','.','.','.','.','.','.','.','.'],
						  ['e ','.','.','.','.','.','.','.','.','.','.'],
						  ['f ','.','.','.','.','.','.','.','.','.','.'],
						  ['g ','.','.','.','.','.','.','.','.','.','.'],
						  ['h ','.','.','.','.','.','.','.','.','.','.'],
						  ['i ','.','.','.','.','.','.','.','.','.','.'],
						  ['j ','.','.','.','.','.','.','.','.','.','.'],
						  ['r']]

            board(num)	# prints board
            global new_coord_1
            new_coord_1 = [0,0] # creates previous attack list
			# player sets up their board by placing their ships
            for i in range(5):
                global length
                length, name,label = length_dict[i] # assigns variables 
                print('The',name,'takes up',length,'spaces.' )
                print('Enter the coordinates for your ships placement.')
                coordinate,vertical = who_play(whos,num) # retrieves the coordinates for the attack
                coordinate,vertical = placement_c(player_1,coordinate,length,vertical,whos) # checks if placement is correct 
                place_ship(player_1,coordinate,length,vertical,label) # places ship
			# prints players board to see their finished result
                board(num)
            ready = input('Ready to switch? press Enter or enter end!') # gives user time to check board and gives option to end game
            if ready == 'end': # ends game
                end([ready])
            print(20*'\n') # privacy for user till player have switched
			# does not move on until user is ready
            switch = input('If you have swtiched say yes:') # when players have switched
			
	###############################################################################################################
        elif num == 2: # player 2's turn
            global opponents_1
            opponents_1 =[['  ','1','2','3','4','5','6','7','8','9','10','c'],
						  ['a ','.','.','.','.','.','.','.','.','.','.'],
						  ['b ','.','.','.','.','.','.','.','.','.','.'],
						  ['c ','.','.','.','.','.','.','.','.','.','.'],
						  ['d ','.','.','.','.','.','.','.','.','.','.'],
						  ['e ','.','.','.','.','.','.','.','.','.','.'],
						  ['f ','.','.','.','.','.','.','.','.','.','.'],
						  ['g ','.','.','.','.','.','.','.','.','.','.'],
						  ['h ','.','.','.','.','.','.','.','.','.','.'],
						  ['i ','.','.','.','.','.','.','.','.','.','.'],
						  ['j ','.','.','.','.','.','.','.','.','.','.'],
						  ['r']]

            global player_2
            player_2 =   [['  ','1','2','3','4','5','6','7','8','9','10','c'],
						  ['a ','.','.','.','.','.','.','.','.','.','.'],
						  ['b ','.','.','.','.','.','.','.','.','.','.'],
						  ['c ','.','.','.','.','.','.','.','.','.','.'],
						  ['d ','.','.','.','.','.','.','.','.','.','.'],
						  ['e ','.','.','.','.','.','.','.','.','.','.'],
						  ['f ','.','.','.','.','.','.','.','.','.','.'],
						  ['g ','.','.','.','.','.','.','.','.','.','.'],
						  ['h ','.','.','.','.','.','.','.','.','.','.'],
						  ['i ','.','.','.','.','.','.','.','.','.','.'],
						  ['j ','.','.','.','.','.','.','.','.','.','.'],
						  ['r']]
            board(num) # prints board
            global new_coord_2
            new_coord_2 = [0,0] # place holder for hits
			# player sets up their board by placing their ships
            for i in range(5):
                length, name,label = length_dict[i] # assigns variables
                print('The',name,'takes up',length,'spaces.' )	
                print('Enter the row and column for placement of your ship.')
                coordinate,vertical = who_play(whos,num) # recieves coordinate
                coordinate,vertical = placement_c(player_2,coordinate,length,vertical,whos) # checks for placment of ship is correct
                place_ship(player_2,coordinate,length,vertical,label) # places ship
                board(num) # prints board
			# for privacy of each player and gives option to end game
            ready = input('Ready to switch? press Enter or enter end!')
            if ready == 'end': #ends game
                end([ready])
            print(20*'\n')
			# does not move on until user is ready
            switch = input('If you have swtiched say yes:')

	###############################################################################################################	

		# Player 1 turn to attack		
        elif num != 1 and num %2==1:
            board(num) # prints their board
            print('Player 1 it is your turn!')
            print('Enter the row and column for your attack!')
            coord = who_play(whos,num)[0] # recieves coordinate for attack
            #w.PlaySound("canon", w.SND_FILENAME) # sound of shots being fired
            correct_move(num,coord,whos) # attaks 
			# checks if player 1 has won
            if end(player_2): 
                break
			# privacy for player and gives option to end game
            user = input('See if you hit or missed and press enter for player twos turn or enter end!')
            if user == 'end': # ends game
                end([user])
            print(20*'\n')
			# does not move on until user is ready
            switch = input('If you have swtiched say yes:')

			
	###############################################################################################################		
		# player 2 turn to attack
        elif num !=2 and num %2==0:	
            board(num) # prints board
            print('Player 2 it is your turn!')
            print('Enter the row and column for your attack!')
            coord = who_play(whos,num)[0] # recieves coordinate
            #w.PlaySound("canon", w.SND_FILENAME) # attack noise
            correct_move(num,coord,whos) # places move
			# checks if player 2 has won
            if end(player_1):
                break
			# privacy for player and gives option to end game
            user = input('See if you hit or missed and press enter for player ones turn or enter end!')
            if user == 'end': # ends game
                end([user])
            print(20*'\n')
			# does not move on until user is ready
            switch = input('If you have swtiched say yes:')
def continue_game():
    """
	no parameters
	continously plays game as long as user would like to
	
	"""
    dict_start = {'yes','no'} # valid answers
    start = input('Would you like to play battleship enter (yes or no)')
    while start not in dict_start: # checks for valid answer
        start = input('Would you like to play battleship enter (yes or no)')	
    while start == 'yes': #if yes runs code
        main() # 
        start = input('Would you like to play again? enter (yes or no)')
        while start not in dict_start:
            start = input('Would you like to play battleship enter (yes or no)')
    if start == 'no': # if no ends code
       end(['end'])
		
continue_game()




