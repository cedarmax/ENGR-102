# -*- coding: utf-8 -*-
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
def board():
	opponents =[['a','.','.','.','.','.','.','.','.','.','.'],
	           ['b','.','.','.','.','.','.','.','.','.','.'],
	           ['c','.','.','.','.','.','.','.','.','.','.'],
	           ['d','.','.','.','.','.','.','.','.','.','.'],
	           ['e','.','.','.','.','.','.','.','.','.','.'],
	           ['f','.','.','.','.','.','.','.','.','.','.'],
	           ['g','.','.','.','.','.','.','.','.','.','.'],
	           ['h','.','.','.','.','.','.','.','.','.','.'],
	           ['i','.','.','.','.','.','.','.','.','.','.'],
			   ['j','.','.','.','.','.','.','.','.','.','.'],
			   ['','1','2','3','4','5','6','7','8','9','10']]
	print('player 2')
	yours = opponents[:]
	for i in opponents: #prints out layout of chessboard before every move
		print(*i, sep ='   ')
	print('player 1')
	for i in yours:
		print(*i, sep = '   ')		
rows = 8
columns = 8
board()







# =============================================================================
# #The following seems to be the accepted method for setting up a program to move through a matrix.
# 
# while True:
#     print('This is the Chessboard')
#     for i in range (rows):
#         for j in range (columns):
#             print(board[i][j], end='')
#         print('') #Required in order to print in columns.
# 
#     print('Where is your piece now?')
#     row = int(input('Row?'))
#     column = int(input('Column?'))
#     row -= 1  #An adustment needed to be made since the row is technically from 0 to 7.
#     column -= 1 #An adustment needed to be made since the column is technically from 0 to 7.
#     if board [row][column] == '.':  #This was required to terminate the program if user accidentially asked to move from a blank space.
#         print('You asked to move from a position where there was no piece, so the game has terminated.')
#         break
#     else:
#         position = board[row][column]
#         board[row][column] = '.'  #This is to replace the position with a dot.
#         print('Where are you moving your piece?')
#         row = int(input('Row?'))
#         column = int(input('Column?'))
#         row -= 1 #Again, an adjustment needed to be made since the row list is actually from 0 to 7.
#         column -= 1 #An adustment needed to be made since the column is technically from 0 to 7.
#         board[row][column] = position
# 
# 
# =============================================================================


































