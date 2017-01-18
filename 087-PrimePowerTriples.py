#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
# Sınır değerini 50 milyonun karekökü civarında almak yeterli güvenlik seviyesini sağlıyor.

from sympy import primerange

LIMIT = 50000000
primes = list(primerange(2,int(LIMIT**0.5)))
sonuc = set()

for a in primes:
    for b in primes:
        for c in primes:
            if(a**2+b**3+c**4<LIMIT):
                sonuc.add(a**2+b**3+c**4)
            else:
                break
print(len(sonuc))
