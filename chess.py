# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:37:14 2023

@author: chamo
"""

# Welcome message and basic dimensions of board
print("")
print("Welcome to my chess game!")
print("")

board_dim = 8
def init_board():
   
    board = [["\u2610" for j in range(8)]for i in range(8)]
    return board

board = init_board()    
#print(board)

# Set the starting position of all of the pieces on the board

#NOTE: White and black Unicode is swapped
# because the black pieces looker whiter than the white pieces

# black pieces
board[0][0]="\u2656"
board[0][7]="\u2656"
board[0][1]="\u2658"
board[0][6]="\u2658"
board[0][2]="\u2657"
board[0][5]="\u2657"
board[0][3]="\u2655"
board[0][4]="\u2654"
for x in range(8):
   board[1][x] = "\u2659"

# white pieces
board[7][0]="\u265C"
board[7][7]="\u265C"
board[7][1]="\u265E"
board[7][6]="\u265E"
board[7][2]="\u265D"
board[7][5]="\u265D"
board[7][3]="\u265B"
board[7][4]="\u265A"
for x in range(8):
   board[6][x] = "\u265F"

pieces = {"Black_Castle":"\u2656","Black_Knight":"\u2658",
          "Black_Bishop":"\u2657","Black_King":"\u2654",
          "Black_Queen":"\u2655","Black_Pawn":"\u2659",
          "White_Castle":"\u265C","White_Knight":"\u265E",
          "White_Bishop":"\u265D","White_Queen":"\u265B",
          "White_King":"\u265A","White_Pawn":"\u265F"}


#print(board)

# This section prints the board in a neat way

rank = [8,7,6,5,4,3,2,1]
file = ["a","b","c","d","e","f","g","h"]
def print_board(board):
   
    print("  ", end= "")
    for c in file:
        print(c+" ", end = " ")
    print()
    for i in range(len(board)):
        print((8-i), end = " ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()

print_board(board)

# This next section asks the player to input the square 
# moved from and the square moved to
win = False
turn = 0
while win == False:
    
    turn += 1
    print("")
    print(f"TURN {turn}")
    print("")
    mov_from = str(input("Which rank and file are you moving from in that order?: (eg: 2d): "))
    print("")
    mov_to = str(input("Which rank and file are you moving to?: (eg: 3d): "))
    print("")
    
    # This section separates the rank and file for each of the above inputs
    
    def move_from():
        from_rank_file = []
        for i in mov_from:
            from_rank_file += [i]
        
        return from_rank_file
    
    from_rank_file = move_from() 
    
    rank_from = from_rank_file[0]
    file_from = from_rank_file[1]
    
    def move_to():
        to_rank_file = []
        for i in mov_to:
            to_rank_file += [i]
    
        return to_rank_file
    
    to_rank_file = move_to() 
     
    rank_to = to_rank_file[0]
    file_to = to_rank_file[1]
    
    
    
    # Transform the human user input to grid coordinates that python understands
    
    row_from = 8 - int(rank_from)
    col_from = file.index(file_from)
    row_to = 8 - int(rank_to)
    col_to = file.index(file_to)
    
    piece = board[row_from][col_from]
    
    # Tell the user what piece they are moving and where to
    
    print(f"You are moving {board[row_from][col_from]} from {mov_from} to {mov_to}")
    print("")
    
    
    # for white pawn legal move check
    
    
    #if move = "valid"
    #if  piece == pieces["Black_Pawn"] and int(rank_to) != (int(rank_from) - 1) and turn !=1: 
        
        
        #print("That move is not legal, make a different move!!")
            
        #print("")
                
    #elif turn == 1 and piece == pieces["Black_Pawn"] and rank_to != int(rank_from) - 2: 
        
        #print("That move is not legal, make a different move!!")
            
        #print("")
        
        
        
      # have passed legal move tests so write the move to the board
        
    board[row_from][col_from] = "\u2610"
    board[row_to][col_to] = piece
        
       #Print the new board with the moved piece
       
    def print_board(board):
       
        print("  ", end= "")
        for c in file:
            print(c+" ", end = " ")
        print()
        for i in range(len(board)):
            print((8-i), end = " ")
            for j in range(len(board[i])):
                print(board[i][j], end = " ")
            print()
    
    print_board(board)
