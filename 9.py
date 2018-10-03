#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:12:47 2017


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


@author: alex

m2-n2
2*m*n
m2+n2

2m2 + 2mn - 1000 = 0


"""

a = 3
b = 4
c = 5

#for x in range(1000,a,-1):
#    for y in range(b, 1000-x):
#        for z in range(c, 1000-x-y):
#            if (x)**2 + (y)**2 == (z)**2:
##                if x + y + z == 1000:
#                print(x*y*z)
#                print(x, y, z)
#                break
#            else: 
#                print('Not found')
#                print(x, y, z)

for m in range(1, 1000):
    for n in range(1, 1000):
        triplet_sum = 2*(m**2) + 2*m*n
        if triplet_sum == 1000:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            print(a, b, c, a*b*c)


