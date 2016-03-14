# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 02:16:10 2016

@author: Rrich
"""

def genPrimes():
    '''Have the generator keep a list of the primes it's generated. 
    A candidate number x is prime if (x % p) != 0 for all earlier primes p.'''
    i=1
    primes=[]
    while(True):
       i += 1
       for p in primes:
          if (i%p == 0):
             break
       else:
          primes.append(i)
          yield i

primeGenerator = genPrimes()
print primeGenerator.next()
print primeGenerator.next()
print primeGenerator.next()
print primeGenerator.next()
print primeGenerator.next()
print primeGenerator.next()