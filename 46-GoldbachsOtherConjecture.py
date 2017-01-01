#!/usr/bin/python3
# -*- coding: utf-8 -*-
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from functions import allprimes
from math import sqrt

def goldbach(n):
    kontrol = allprimes(n)
    for p in kontrol:
        if(int(sqrt((n-p)/2))==sqrt((n-p)/2)):
            return(1)
            break
    else:
        return(0)

asal = allprimes(10000)

for n in range(9,10000,2):
    if(asal.count(n)==1):
        continue
    if(goldbach(n)==0):
        print(n)
        break
