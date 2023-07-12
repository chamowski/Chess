# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:57:57 2023

@author: chamo
"""

#rank = [8,7,6,5,4,3,2,1]

def rank_file():
    rank = ["8","7","6","5","4","3","2","1"]
    file = ["a","b","c","d","e","f","g","h"]
    board = []
    for i in rank:
        board = board + [[j+i for j in file]]
        
    return board
board = rank_file()

print(board) 