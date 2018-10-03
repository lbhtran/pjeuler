#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:16:43 2017


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


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
 
print(primeSieve(1200)[195])

print(primeSieve(120000)[10000])