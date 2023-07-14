# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:05:48 2023

@author: chamo
"""

print("some other  things")


def f(x):
    return x**2

print(f(5))
print(*[f(i) for i in range(10)])