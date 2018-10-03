#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:08:05 2017

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: alex
"""

def sum_of_squares(n):
    list = []
    for i in range(n+1):
        list.append(i**2)
    return sum(list)

#print(sum_of_squares(10))

def square_of_sum(n):
    k = sum(range(n+1))
    return k**2

#print(square_of_sum(10))

def sum_squares_diff(n):
    return abs(sum_of_squares(n) - square_of_sum(n))

print(sum_squares_diff(100))