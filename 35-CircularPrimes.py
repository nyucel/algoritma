#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from functions import isprime

sonuc = 13
for n in range(101,1000000,2):
    if(isprime(n)==0):
        continue
    for p in range(len(str(n))):
        if(isprime(int(n))==0):
            break
        n=list(str(n))
        n.append(n[0])
        n.remove(n[0])
        n=''.join(str(i) for i in n)
    else:
        sonuc +=1
print(sonuc)
