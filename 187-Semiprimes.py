#!/usr/bin/python3
# -*- coding: utf-8 -*-
# A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.
# There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.
# How many composite integers, n < 10^8, have precisely two, not necessarily distinct, prime factors?
# 10^8'den yarısından küçük her asal için kendinden küçük eşit asal sayılarla çarpımından oluşturulan sayılar sayıldığında aranan sonuç bulunmuş oluyor.

from sympy import primepi
from sympy import primerange

sonuc = 0

LIMIT = 10**8
primes = primerange(2,LIMIT//2)

for n in primes:
    if(n<LIMIT**(0.5)):
        m = primepi(n)
    else:
        m = primepi(LIMIT//n)
    sonuc += m
print(sonuc)
