#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:51:05 2017

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

@author: alex
"""

def reversenumber(Number):
    Reverse = 0    
    while(Number > 0):    
        Remainder = Number %10    
        Reverse = (Reverse *10) + Remainder    
        Number = Number //10    
    return Reverse

i = 999
n = 0
for i in reversed(range(100,999)):
    for j in reversed(range(100,999)):
        number = i * j
        if number == reversenumber(number) and number > n:
            n = number
            maxi = i
            maxj = j
    i = i - 1
print(maxi, maxj, n)