#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

from functions import allprimes
primes=allprimes(10000)[168:]
sonuc=0
for n in primes:
    for m in range(2,5000-int(n/2),2):
        if(primes.count(n+m)==1 and primes.count(n+2*m)==1):
            for i in str(n):
                if(str(n+m).count(i)==0 or str(n+2*m).count(i)==0):
                    break
            else:
                for j in str(n+m):
                    if(str(n+2*m).count(j)==0 or str(n).count(j)==0):
                        break
                else:
                    for k in str(n+2*m):
                        if(str(n).count(k)==0 or str(n+m).count(k)==0):
                            break
                    else:
                        print(n,n+m,n+2*m)
                        sonuc += 1
    if(sonuc==2):
        break
