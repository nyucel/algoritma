#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.
# Find the sum of all positive integers n not exceeding 100 000 000 such that for every divisor d of n, d+n/d is prime.

from functions import allprimes

LIMIT = 10**8
primes = allprimes(LIMIT)

def kontrol(n):
    if n%4==0 : return 0
    r=int(n**0.5)+1
    for i in range(1,r+1):
        if(n%i==0):
            if i+n/i not in s:
                return 0
    return 1

s=set(primes)
toplam=sum(p-1 for p in primes if kontrol(p-1))

print(toplam)
