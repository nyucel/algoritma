#!/usr/bin/python3
# -*- coding: utf-8 -*-
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

from sympy import binomial
sayi = 0
for n in range(1,101):
    for r in range(1,101):
        if binomial(n,r)>1000000:
            sayi += 1
print(sayi)
