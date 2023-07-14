# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:37:14 2023

@author: chamo
----------------------------------
   GAME STILL IN DEVELOPMENT
--------------------------------

"""
from starting_pieces import starting_pieces
# Welcome message and basic dimensions of board


# CONSTANTS

board_dim = 8

pieces = {"Black_Castle":"\u2656","Black_Knight":"\u2658",
          "Black_Bishop":"\u2657","Black_King":"\u2654",
          "Black_Queen":"\u2655","Black_Pawn":"\u2659",
          "White_Castle":"\u265C","White_Knight":"\u265E",
          "White_Bishop":"\u265D","White_Queen":"\u265B",
          "White_King":"\u265A","White_Pawn":"\u265F"}

colour = {"\u2656":"Black","\u2658":"Black",
          "\u2657":"Black","\u2654":"Black",
          "\u2655":"Black","\u2659":"Black",
          "\u265C":"White","\u265E":"White",
          "\u265D":"White","\u265B":"White",
          "\u265A":"White","\u265F":"White"}

rank = [8,7,6,5,4,3,2,1]
file = ["a","b","c","d","e","f","g","h"]

# FUNCTIONS

#Set up list of lists for initial board

def init_board():
   
    board = [["\u2610" for j in range(8)]for i in range(8)]
    
    board = starting_pieces(board)
    return board

# Separates player input string into list

def move_from(mf):
    from_rank_file = []
    for i in mf:
        from_rank_file += [i]
        
    return from_rank_file

def move_to(mt):
    to_rank_file = []
    for i in mt:
        to_rank_file += [i]

    return to_rank_file

# This section prints the board in a neat way

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

def main():
    
    print("")
    print("Welcome to my chess game!")
    print("")
    board = init_board() 
    print_board(board)
    
    # This next section asks the player to input the square 
    # moved from and the square moved to
    win = False
    turn = 0
    
    while win == False:
        
        turn += 1
      
        legal = False
        col = False
        
        while (legal == False) or (col == False):
            
            if int(turn)%2 != 0 or turn == 1:
                print("")
                print(f"TURN {turn}, White to move")
                print("")
            elif int(turn)%2 == 0:
                print("")
                print(f"TURN {turn}, Black to move")
                print("")
            
            print("")
            move_from_input = str(input("Which rank and file are you moving from in that order?: (eg: 2d): "))
            print("")
            move_to_input = str(input("Which rank and file are you moving to?: (eg: 3d): "))
            print("")
        
            # This section separates the rank and file for each of the above inputs 
            #by running them through their functions above
            
            from_rank_file = move_from(move_from_input) 
        
            rank_from = from_rank_file[0]
            file_from = from_rank_file[1]
        
            to_rank_file = move_to(move_to_input) 
         
            rank_to = to_rank_file[0]
            file_to = to_rank_file[1]
                               
            # Transform the human user input to grid coordinates that python understands
        
            row_from = 8 - int(rank_from)
            col_from = file.index(file_from)
            row_to = 8 - int(rank_to)
            col_to = file.index(file_to)
                       
            #Get the piece type
            
            piece = board[row_from][col_from]
                    
            # Tell the user what piece they are moving and where to
        
            print(f"You are moving {board[row_from][col_from]} from {move_from_input} to {move_to_input}")
            print("")
        
            
            if colour[piece] == "White" and (turn == 1 or turn%2 != 0):
                col = True
            elif colour[piece] == "Black" and turn%2 ==0:
                col = True
            else: 
                print_board(board)
                print("")
                print(f"It's not {colour[piece]}'s turn !!")
                print("")
                
            
        
                            
            
            #FOR TESTING ONLY
            #legal = True
            #print("rank_from",rank_from, "rank_to",rank_to)
            #print("row_from",rank_from, "row_to",rank_to)
            
             
             
            # Check if the piece type move is legal
             
            # for pawn legal move check
         
            """
             
            if  piece == pieces["Black_Pawn"] and int(rank_to) == (int(rank_from) - 1) and turn !=1: 
                legal = True
             
            elif piece == pieces["Black_Pawn"] and int(rank_to) == (int(rank_from) - 2) and turn ==1:
                legal = True             
            
            elif  piece == pieces["White_Pawn"] and int(rank_to) == (int(rank_from) + 1) and turn !=1: 
                legal = True
             
            elif piece == pieces["White_Pawn"] and int(rank_to) == ((int(rank_from) + 2) or (int(rank_from) + 1)) and turn ==1:
                legal = True
            else: 
                print("")
                print_board(board)
                print("That move is not legal, make a different move !!")
                print("")    
                     
                 #elif turn == 1 and piece == pieces["Black_Pawn"] and rank_to != int(rank_from) - 2: 
             
                     #print("That move is not legal, make a different move!!")
                 
                     #print("")
             
             
            """   
             
            
         
        # If the code gets to this point, we have passed legal move and turn 
        #tests so write the move to the board
         
        board[row_from][col_from] = "\u2610"
        board[row_to][col_to] = piece
         
        #Print the new board with the moved piece
        
        print_board(board)
     
        

main()