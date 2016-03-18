# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 02:16:10 2016

@author: Rrich
"""

def genPrimes():
    '''The generator keeps a list of the primes it has generated. 
    A candidate number i is prime if (i % p) != 0 for all earlier primes p.'''
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
for p in range(10):                        # will print first 10 prime numbers
    print primeGenerator.next()
