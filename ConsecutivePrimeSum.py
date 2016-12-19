#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The prime 41, can be written as the sum of six consecutive primes:
#           41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from functions import isprime
maks=1
primes=[]
for i in range(2,1000000):
    if isprime(i)==1:
        primes.append(i)
for p in range(100,600):
    for i in range(len(primes)-p-1):
        sums = 0
        for j in range(p):
            sums += primes[i+j]
        if (i==1) and sums>primes[-1]:
            break
        if(primes.count(sums)==1):
            maks=sums
print(maks)
