#!/usr/bin/python3
# -*- coding: utf-8 -*-

import primesieve

LIMIT = 10**10
R = int(LIMIT**(1/2))
counter = 0

for n in range(1, R+1):
    counter += primesieve.count_primes(n, LIMIT//n)

print(LIMIT-counter)
