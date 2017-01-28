#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=348

from math import sqrt
ALIMIT = 5229225
ULIMIT = 10**9
DLIMIT = int(ULIMIT**(1/3))
sonuc = set()

for n in range(ALIMIT, ULIMIT):
    if(n%10==0):
        continue
    cozum = 0
    if(str(n)==str(n)[::-1]):
        for m in range(2, DLIMIT):
            if(cozum==4):
                sonuc.add(n)
                break
            if(n-m**3<0):
                break
            p = sqrt(n-m**3)
            if(p==int(p)):
                cozum += 1
    if(len(sonuc)==5):
        break
print(sum(sonuc))
