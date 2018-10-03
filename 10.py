#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:54:28 2018


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


@author: alex
"""

import math

def primeSieve(sieveSize):

     # Returns a list of prime numbers calculated using

     # the Sieve of Eratosthenes algorithm.

     sieve = [True] * sieveSize
     sieve[0] = False # zero and one are not prime numbers
     sieve[1] = False
     # create the sieve
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i
     # compile the list of primes
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)
     return primes
 
print(primeSieve(10))

print(sum(primeSieve(2000000)))