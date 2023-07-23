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
          "White_King":"\u265A","White_Pawn":"\u265F","\u2610":"Empty"}

colour = {"\u2656":"Black","\u2658":"Black",
          "\u2657":"Black","\u2654":"Black",
          "\u2655":"Black","\u2659":"Black",
          "\u265C":"White","\u265E":"White",
          "\u265D":"White","\u265B":"White",
          "\u265A":"White","\u265F":"White","\u2610":"Empty"}

ptype = {"\u2656":"Castle","\u2658":"Knight",
          "\u2657":"Bishop","\u2654":"King",
          "\u2655":"Queen","\u2659":"Pawn",
          "\u265C":"Castle","\u265E":"Knight",
          "\u265D":"Bishop","\u265B":"King",
          "\u265A":"Queen","\u265F":"Pawn","\u2610":"Empty"}

rank = ["8","7","6","5","4","3","2","1"]
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
    Whites_won = []
    Blacks_won = []
    while win == False:
        
        turn += 1
      
        legal = False
        col = False
        
        
        while (legal == False):
            
            if int(turn)%2 != 0 or turn == 1:
                print("")
                print(f"TURN {turn}, White to move")
                print("")
            elif int(turn)%2 == 0:
                print("")
                print(f"TURN {turn}, Black to move")
                print("")
            
            print("")
            
            # Input resquests and validity checking
            
            # Move from:
                
            inp_chk = False
            
            col = False
            
            while inp_chk == False or col == False:
                
                move_from_input = str(input("Which rank and file are you moving from in that order?: (eg: 2d): "))
                print("")
                
                # Check length of input
                
                if len(move_from_input) != 2:
                    print("")
                    print(f"'{move_from_input}' is not a valid entry...")
                    print("")
                    continue
                
                # Check contents of input
                          
                if move_from_input[0] in rank and move_from_input[1] in file:
                    inp_chk = True
                    
                    # This section separates the rank and file data of the above inputs 
                    # by running them through move_from function above
                    
                    from_rank_file = move_from(move_from_input) 
                                               
                    rank_from = from_rank_file[0]
                    file_from = from_rank_file[1]
                    
                    # Transform the human user input to grid coordinates for list of lists
                
                    row_from = 8 - int(rank_from)
                    col_from = file.index(file_from)
                    
                    # Get the piece type
                    
                    piece = board[row_from][col_from]
                else:
                    print("")
                    print(f"'{move_from_input}' is not a valid entry...")
                    print("")
                    continue
                    
                # Check that the input is not an empty square
                
                if colour[piece] == "Empty":
                    print("")
                    print(f"'{move_from_input}' is an empty square...")
                    print("")
                    continue
                    
                # Check that the correct colour is being moved                
                
                if colour[piece] == "White" and (turn == 1 or turn%2 != 0):
                    col = True
                elif colour[piece] == "Black" and turn%2 ==0:
                    col = True
                else: 
                    print_board(board)
                    print("")
                    print(f"It's not {colour[piece]}'s turn !!")
                    print("")
                    
                    if int(turn)%2 != 0 or turn == 1:
                        print("")
                        print(f"TURN {turn}, White to move")
                        print("")
                    elif int(turn)%2 == 0:
                        print("")
                        print(f"TURN {turn}, Black to move")
                        print("")
                    
                    print("")
                        
            # Move to:
                        
            inp_chk = False
            
            while inp_chk == False:
                
                move_to_input = str(input("Which rank and file are you moving to?: (eg: 3d): "))
                print("")
                            
                if move_to_input[0] in rank and move_to_input[1] in file:
                    inp_chk = True
                        
                    to_rank_file = move_to(move_to_input) 
                    
                    rank_to = to_rank_file[0]
                    file_to = to_rank_file[1]
                
                    row_to = 8 - int(rank_to)
                    col_to = file.index(file_to)
                else:
                    print("")
                    print(f"'{move_to_input}' is not a valid entry...")
                    print("")
            
            # Tell the user what piece they are moving and where to
        
            print(f"You are moving {board[row_from][col_from]} from {move_from_input} to {move_to_input}")
            print("")
        
            
            
                
            #FOR TESTING ONLY
            
            #print("rank_from",rank_from, "rank_to",rank_to)
            #print("row_from",row_from, "row_to",row_to)
            #print("file_from",file_from, "file_to",file_to)
            #print("col_from",col_from, "col_to",col_to)
                                
            
            
            """
            #____________________________________________________
             
            # Check if the piece type move is legal
             
                     
            # List all legal moves for each piece
            
            """
            
            #FOR TESTING ONLY
            #legal = True
            #print("rank_from",rank_from, "rank_to",rank_to)
            #print("row_from",row_from, "row_to",row_to)
            #print("file_from",file_from, "file_to",file_to)
            #print("col_from",col_from, "col_to",col_to)
            
            
            #PAWNS
            #____________________________________________________
            
            
            if  piece == pieces["White_Pawn"] and int(row_to) == (int(row_from) - 1) and row_from != 6 and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610": 
                legal = True
             
            elif piece == pieces["White_Pawn"] and (int(row_to) == int(row_from) - 2 or int(row_to) == int(row_from) - 1) and row_from == 6 and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610":
                legal = True   
                
            elif piece == pieces["White_Pawn"] and int(row_to) == (int(row_from) - 1) and int(col_to) == int(col_from) + 1 and colour[board[row_to][col_to]] == "Black":
                legal = True  
                if board[row_to][col_to] != "\u2610":
                    print("")
                    Blacks_won += board[row_to][col_to]
                    print(f"You took Black's {ptype[board[row_to][col_to]]}!")
                    Blacks_won
                    print("")
                else: break    
            elif piece == pieces["White_Pawn"] and int(row_to) == (int(row_from) - 1) and int(col_to) == int(col_from) - 1  and colour[board[row_to][col_to]] == "Black":
                legal = True 
                if board[row_to][col_to] != "\u2610":
                    print("")
                    Blacks_won += board[row_to][col_to]
                    print(f"You took Black's {ptype[board[row_to][col_to]]}!")
                    Blacks_won
                    print("")
                else: break 
                    
            elif piece == pieces["Black_Pawn"] and int(row_to) == (int(row_from) + 1) and row_from != 1 and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610": 
                legal = True
             
            elif piece == pieces["Black_Pawn"] and (int(row_to) == int(row_from) + 2 or int(row_to) == int(row_from) + 1) and row_from == 1 and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610":
                legal = True 
                
            elif piece == pieces["Black_Pawn"] and int(row_to) == (int(row_from) + 1) and int(col_to) == int(col_from) + 1 and colour[board[row_to][col_to]] == "White":
                legal = True  
                if board[row_to][col_to] != "\u2610":
                    print("")
                    Whites_won += board[row_to][col_to]
                    print(f"You took Black's {ptype[board[row_to][col_to]]}!")
                    Whites_won
                    print("")
                else: break            
                
            elif piece == pieces["Black_Pawn"] and int(row_to) == (int(row_from) + 1) and int(col_to) == int(col_from) - 1 and colour[board[row_to][col_to]] == "White":
                legal = True  
                if board[row_to][col_to] != "\u2610":
                    print("")
                    Whites_won += board[row_to][col_to]
                    print(f"You took Black's {ptype[board[row_to][col_to]]}!")
                    Whites_won
                    print("")
                else: break
            
             
             
           
                 
            
             #_____________________________________________________________
             #KNIGHTS
            
            
            elif ptype[piece] == "Knight" and (int(row_to) == (int(row_from) - 1) or int(row_to) == (int(row_from) + 1)) and (int(col_to) == int(col_from) - 2 or int(col_to) == int(col_from) + 2) and board[row_to][col_to] == "\u2610":
                legal = True
                
            elif ptype[piece] == "Knight" and (int(row_to) == (int(row_from) - 2) or int(row_to) == (int(row_from) + 2)) and (int(col_to) == int(col_from) - 1 or int(col_to) == int(col_from) + 1) and board[row_to][col_to] == "\u2610":   
                legal = True
                
            elif ptype[piece] == "Knight" and (int(row_to) == (int(row_from) - 1) or int(row_to) == (int(row_from) + 1)) and (int(col_to) == int(col_from) - 2 or int(col_to) == int(col_from) + 2) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                    
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)
                    print("")
                    
            elif ptype[piece] == "Knight" and (int(row_to) == (int(row_from) - 2) or int(row_to) == (int(row_from) + 2)) and (int(col_to) == int(col_from) - 1 or int(col_to) == int(col_from) + 1) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)
                    
             
            #__________________________________________________________     
            #KING    
                
            elif ptype[piece] == "King" and (int(row_to) == (int(row_from) - 1) or int(row_to) == (int(row_from) + 1)) and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610":
                legal = True            
                
            elif ptype[piece] == "King" and (int(row_to) == (int(row_from) - 1) or int(row_to) == (int(row_from) + 1)) and int(col_to) == int(col_from) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                    
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)
                    print("")
            
            elif ptype[piece] == "King" and int(row_to) == int(row_from) and (int(col_to) == int(col_from) - 1 or int(col_to) == int(col_from) + 1) and board[row_to][col_to] == "\u2610":   
                legal = True
                
            elif ptype[piece] == "King" and int(row_to) == int(row_from) and (int(col_to) == int(col_from) - 1 or int(col_to) == int(col_from) + 1) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)     
                    
            elif ptype[piece] == "King" and (int(row_to) == (int(row_from) - 1) or int(row_to) == (int(row_from) + 1)) and (int(col_to) == int(col_from) - 1 or int(col_to) == int(col_from) + 1) and board[row_to][col_to] == "\u2610":   
                legal = True
                
            elif ptype[piece] == "King" and (int(row_to) == (int(row_from) - 1) or int(row_to) == (int(row_from) + 1)) and (int(col_to) == int(col_from) - 1 or int(col_to) == int(col_from) + 1) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)     
                    
            # This is the global else for all of the legal moves                
             
            else:
                print("")
                print_board(board)
                print("")
                print("That move is not legal, make a different move !!")
                print("")  
              
            #_____________________________________________________________
            # QUEEN 
            """
            
            elif ptype[piece] == "Queen" and (int(row_to) == (int(row_from) - range(7)) or int(row_to) == (int(row_from) + range(7))) and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610":
                legal = True            
                
            elif ptype[piece] == "Queen" and (int(row_to) == (int(row_from) - range(7)) or int(row_to) == (int(row_from) + range(7))) and int(col_to) == int(col_from) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                    
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)
                    print("")
            
            elif ptype[piece] == "Queen" and int(row_to) == int(row_from) and board[row_to][col_to] == "\u2610":   
                legal = True
                
            elif ptype[piece] == "Queen" and int(row_to) == int(row_from) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)     
                    
            elif ptype[piece] == "Queen" and int(col_to) == int(col_from) and board[row_to][col_to] == "\u2610":   
                legal = True
                
            elif ptype[piece] == "Queen" and int(col_to) == int(col_from) and board[row_to][col_to] != "\u2610" and colour[piece] != colour[board[row_to][col_to]]:
                legal = True
                print("")                
                print(f"You took {colour[board[row_to][col_to]]}'s {ptype[board[row_to][col_to]]}!")
                if colour[board[row_to][col_to]] == "White":
                    Whites_won += board[row_to][col_to]
                    print(Whites_won)
                    print("")
                elif colour[board[row_to][col_to]] == "Black":
                    Blacks_won += board[row_to][col_to]
                    print(Blacks_won)      
        
            """                 
                     
           
            
        
          
                
        # If the code gets to this point, we have passed legal move and turn 
        #tests so write the move to the board
         
        board[row_from][col_from] = "\u2610"
        board[row_to][col_to] = piece
         
        #Print the new board with the moved piece
        
        print_board(board)
     
        

main()