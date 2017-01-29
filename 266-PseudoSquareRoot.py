#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=266

from sympy import primerange
from math import sqrt
from bisect import bisect_left

primes = list(primerange(2,190))

p = 1
for n in primes:
    p = p*n

kok = sqrt(p)

def euler(n):
    nrs = {1}
    for m in primes[n::2]:
        nrs |= {nr*m for nr in nrs}
    return(sorted(nrs))

nrs1 = euler(0)
nrs2 = euler(1)

maxpsqr = 0

for m in nrs1:
    psqr = nrs2[bisect_left(nrs2, kok/m) - 1] * m
    maxpsqr = max(maxpsqr, psqr)

print(maxpsqr%10**16)
