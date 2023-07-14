# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:05:48 2023

@author: chamo
"""

print("some other  things")



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
    