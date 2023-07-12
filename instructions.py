# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:45:21 2023

@author: chamo
"""


# NOTE: when using a function, return the local variable and assign the 
#the name of the function to the name of the variable you are taking out
#of the function
"""
1. Defs. Make a file named defs.py, with one variable defined: board_dim = 3. 
    In the same folder make another file called tic_tac_toe.py, importing defs.py. 
    In the tic_tac_toe file, print:
        "The board dimensions are", board_dim, "x", board_dim

 
     
2. init_board. In tic_tac_toe.py, write a function called init_board, which
    takes no arguments, and returns a NxN list where every element is "_",
    and N is the board dimension.
Example with N=3:
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    
    
3. print_board. Make a new file called printing.py, and write a function called
    print_board, which takes board as an argument, and nicely prints the board.
    You may decide how you would nicely print the board. To get you started:
        
for row in range(len(board)):
    for col in range(len(board)):
        print(board[row][col], end = "")
    print()
    
For example, try to make something that would display this:
    
  1 2 3
1 _ O _
2 X X _
3 _ X O
    

4. Write a function called 'is_piece' that takes a string of length 1 as
    an argument, and returns True if it is "X" or "O", and False otherwise. 



5. Write a main function that does the following:
    - Prints a message introducing the game ("This is tic tac toe!")
    - make a variable called player_turn, and set it to "X"
    - initialises the board and stores it in the variable 'board'
    
    - In a loop: 
        - print the board nicely
        - tell the user whose turn it is (either "X" or "O")
        - tell the user the valid column/row numbers like (1..3) for board_dim = 3
        - ask the user to enter the column and row,
        - update the board to put their player token on the board ("X" or "O")
        - update the player token to change players ("X" becomes "O", vice versa)
        
    
    
6. Edit the main function so that if a player attempts to place their token
    where there already is a token, ask them to try to take their turn again.
    
    
7. Write a function called is_full(board), that takes the board as the argument,
    and returns True if the board is full (there are no more empty spaces), 
    and False if there are any empty spaces where players can place their tokens. 
    
    
8. Define a function called check_victory that takes the board as the argument,
    which will be used to check if either player has won the game. 
    For now, return "StaleMate" if the board is full, and None if it is not.
    Later on, this function will be edited so that it returns "X" if player X  
    has won, and "O" if player O has won. 


9. Edit the main function so that, after a player successfully places their token,
    the check_victory function is called. If the function returns "StaleMate",
    print a message saying that no one wins, and end the game. If the function returns
    either "X" or "O", print a message announcing the winner, and end the game.
    If the function returns None, continue on with the game. 
    
10. Edit the check_victory function so that it now checks for horizontal wins. 
    For example, if a specific row has all "X", then return "X", as this
    means that player "X" has won. 
    
    Make sure the check_victory function does not return "StaleMate" if a player
    has a horizontal win on a full board!
        
11. Edit the check_victory function so that it now checks for vertical wins. 


12. Edit the check_victory function so that it now checks for diagonal wins. 
    (There are only two diagonals, regardless of board size). 
    
    
Extra: Edit the main function so that it can handle bad user inputs, such as
    rows or columns not on the board, or inputs that aren't valid numbers. 


"""