# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Erwin Luevano
#               Cedar Maxwell
#               Alex Torres
#               Muhammad Amer 
# Section:	ENGR 102-537
# Assignment:	Battleship
# Date:	  	11 December 2019

import random as r
import numpy as np
opponents =[['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
	   ['.','.','.','.','.','.','.','.','.','.']]
print('player 2')
yours = opponents[:]
for i in opponents: #prints out layout of chessboard before every move
	print(*i, sep ='  ')
print('player 1')
for i in yours:
	print(*i, sep = '  ')		

def rules():
	'''This function will be run every time a move is made, checking if the move is valid'''

def CPUBoardCreation():
	'''This function will create the board if the player chooses to play the computer.'''
	
def PlayerBoardCreation():
	'''This function will prompt the player to place his five pieces.'''
	Carrier()
	Battleship()
	Cruiser()
	Submarine()
	Destroyer()
	
ef carrier(coordinate,direction):
	yours[coordinate[0]][coordinate[1]] = 'C'
	if direction == 'l':
		for i in range(1,5):
			yours[coordinate[0]][coordinate[1]-i] = 'C'
	elif direction == 'r':
		for i in range(1,5):
			yours[coordinate[0]][coordinate[1]+i] = 'C'
	elif direction == 'd':
		for i in range(1,5):
			yours[coordinate[0]+i][coordinate[1]] = 'C'
	elif direction == 'u':
		for i in range(1,5):
			yours[coordinate[0]-i][coordinate[1]] = 'C'

def battleship(coordinate,direction):
	yours[coordinate[0]][coordinate[1]] = 'B'
	if direction == 'l':
		for i in range(1,4):
			yours[coordinate[0]][coordinate[1]-i] = 'B'
	elif direction == 'r':
		for i in range(1,4):
			yours[coordinate[0]][coordinate[1]+i] = 'B'
	elif direction == 'd':
		for i in range(1,4):
			yours[coordinate[0]+i][coordinate[1]] = 'B'
	elif direction == 'u':
		for i in range(1,4):
			yours[coordinate[0]-i][coordinate[1]] = 'B'

def destroyer(coordinate,direction):
	yours[coordinate[0]][coordinate[1]] = 'D'
	if direction == 'l':
		for i in range(1,3):
			yours[coordinate[0]][coordinate[1]-i] = 'D'
	elif direction == 'r':
		for i in range(1,3):
			yours[coordinate[0]][coordinate[1]+i] = 'D'
	elif direction == 'd':
		for i in range(1,3):
			yours[coordinate[0]+i][coordinate[1]] = 'D'
	elif direction == 'u':
		for i in range(1,3):
			yours[coordinate[0]-i][coordinate[1]] = 'D'

def submarine(coordinate,direction):
	yours[coordinate[0]][coordinate[1]] = 'C'
	if direction == 'l':
		for i in range(1,3):
			yours[coordinate[0]][coordinate[1]-i] = 'C'
	elif direction == 'r':
		for i in range(1,3):
			yours[coordinate[0]][coordinate[1]+i] = 'C'
	elif direction == 'd':
		for i in range(1,3):
			yours[coordinate[0]+i][coordinate[1]] = 'C'
	elif direction == 'u':
		for i in range(1,3):
			yours[coordinate[0]-i][coordinate[1]] = 'C'

def patrol_boat(coordinate,direction):
	yours[coordinate[0]][coordinate[1]] = 'P'
	if direction == 'l':
		yours[coordinate[0]][coordinate[1]-1] = 'P'
	elif direction == 'r':
		yours[coordinate[0]][coordinate[1]+1] = 'P'
	elif direction == 'd':
		yours[coordinate[0]+1][coordinate[1]] = 'P'
	elif direction == 'u':
		yours[coordinate[0]-1][coordinate[1]] = 'P'


coordinate = np.array(input('Enter the coordinate Ex:(1,2): ').split(','),dtype = int)-1
direction = input('Enter the direction of your piece: ')
carrier(coordinate,direction)
coordinate = np.array(input('Enter the coordinate Ex:(1,2): ').split(','),dtype = int)-1
direction = input('Enter the direction of your piece: ')
battleship(coordinate,direction)
coordinate = np.array(input('Enter the coordinate Ex:(1,2): ').split(','),dtype = int)-1
direction = input('Enter the direction of your piece: ')
destroyer(coordinate,direction)
coordinate = np.array(input('Enter the coordinate Ex:(1,2): ').split(','),dtype = int)-1
direction = input('Enter the direction of your piece: ')
patrol_boat(coordinate,direction)
coordinate = np.array(input('Enter the coordinate Ex:(1,2): ').split(','),dtype = int)-1
direction = input('Enter the direction of your piece: ')
submarine(coordinate,direction)


for i in yours:
	print(*i,sep='  ')
def moves():
	'''This function will initiate each move'''

#The following seems to be the accepted method for setting up a program to move through a matrix.
'''
while True:
    print('This is the Chessboard')
    for i in range (rows):
        for j in range (columns):
            print(board[i][j], end='')
        print('') #Required in order to print in columns.

    print('Where is your piece now?')
    row = int(input('Row?'))
    column = int(input('Column?'))
    row -= 1  #An adustment needed to be made since the row is technically from 0 to 7.
    column -= 1 #An adustment needed to be made since the column is technically from 0 to 7.
    if board [row][column] == '.':  #This was required to terminate the program if user accidentially asked to move from a blank space.
        print('You asked to move from a position where there was no piece, so the game has terminated.')
        break
    else:
        position = board[row][column]
        board[row][column] = '.'  #This is to replace the position with a dot.
        print('Where are you moving your piece?')
        row = int(input('Row?'))
        column = int(input('Column?'))
        row -= 1 #Again, an adjustment needed to be made since the row list is actually from 0 to 7.
        column -= 1 #An adustment needed to be made since the column is technically from 0 to 7.
        board[row][column] = position
'''
