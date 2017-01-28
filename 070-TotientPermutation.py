#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=70

from sympy import totient

LIMIT = 10**7
oran = 42

for n in range(2,LIMIT):
    to = totient(n)
    for p in set(str(n)):
        if(str(n).count(p)!=str(to).count(p)):
            break
    else:
        if(set(str(n))==set(str(to))):
            if(len(set(str(n)))==len(set(str(to)))):
                if(n/to<oran):
                    oran = n/to
                    enkucuk = n
print(enkucuk)
