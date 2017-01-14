#!/usr/bin/python3
# -*- coding: utf-8 -*-
# A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.
# Let us consider repunits of the form R(10^n).
# Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17. Yet there is no value of n for which R(10^n) will divide by 19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10^n).
# Find the sum of all the primes below one-hundred thousand that will never be a factor of R(10^n).
# https://en.wikipedia.org/wiki/Repunit adresinden de görülebileceği gibi bu sayılar R(n)=10^n-1 şeklinde yazılabiliyor.

from sympy import primerange

primes = primerange(2,100000)

bolen = 3
L = 10**20

for n in primes:
    if(pow(10, L, n) != 1):
        bolen += n
print(bolen)

