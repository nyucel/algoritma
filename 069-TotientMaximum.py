#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

from fractions import gcd
def totient(n):
    sonuc=1
    for i in range(2,n):
        if(gcd(n,i)==1):
            sonuc += 1
    return(n/sonuc)

ebn=[]
for n in range(2,1000000,2):
    if(n%3!=0 or n%5!=0 or n%7!=0 or n%11!=0 or n%13!=0 or n%17!=0):
        ebn.append(1)
        continue
    ebn.append(totient(n))
print(2*ebn.index(max(ebn))+2)
