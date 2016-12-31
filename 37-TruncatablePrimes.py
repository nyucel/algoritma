#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from functions import allprimes

primes=allprimes(750000)

rightprimes = []
for n in primes[4:]:
    temp = n
    n=list(str(n))
    for i in range(1,len(n)):
        n.pop()
        n=''.join(str(i) for i in n)
        if(primes.count(int(n))==0):
            break
        n=list(str(n))
    else:
        rightprimes.append(temp)

leftprimes =[]
for n in rightprimes:
    temp = n
    n=list(str(n))
    for i in range(1,len(n)):
        n.remove(n[0])
        n=''.join(str(i) for i in n)
        if(primes.count(int(n))==0):
            break
        n=list(str(n))
    else:
        leftprimes.append(temp)

print(sum(leftprimes))
