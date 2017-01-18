#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Euler discovered the remarkable quadratic formula:
#     n^2+41n+n+41
#    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41n=41,41^2+41+41 is clearly divisible by 41.
#     The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#     Considering quadratics of the form:
#         n^2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000
#         where |n||n| is the modulus/absolute value of nn
#        e.g. |11|=11|11|=11 and |−4|=4|−4|=4
#        Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from functions import allprimes
from functions import isprime

def quadratic(a,b):
    primecount = 0
    for n in range(100):
        if(isprime(n**2+a*n+b)==1):
            primecount += 1
        else:
            break
    return(primecount)

blist = allprimes(1000)
maxab = 1
sonuc = None

for a in range(-999,1000):
    for b in blist:
        if(quadratic(a,b)>maxab):
            maxab = quadratic(a,b)
            sonuc = a*b
print(sonuc)
