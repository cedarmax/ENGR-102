# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names:          Cedar Maxwell
#                 Muhammad Amer
#                 David Simpson
# Section:        537
# Assignment:     Lab 7, Activity 3
# Date:           20 October 2019
 
#The following is intended to follow the sample printout in the lab instructions.

board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]


rows = 8
columns = 8

#The following seems to be the accepted method for setting up a program to move through a matrix.

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
              
    
