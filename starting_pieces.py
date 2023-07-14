# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:00:28 2023

@author: chamo
"""

def starting_pieces(board):
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
    #board[1]["\u265F" for x in range(8)]
    return board
