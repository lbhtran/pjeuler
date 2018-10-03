#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:36:47 2017


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


@author: alex
"""

def gcd(a, b):
    while b>0:
        a, b = b, a % b
    return a

def lcm(a, b):
    value = a * b //gcd(a, b)
    return value


print(reduce(lambda x, y: lcm(x, y), range(1,21)))