#!/usr/bin/python3
# -*- coding: utf-8 -*-
# a^2+b^2=c^2 şeklindeki bütün pisagor üçlüleri s>t>0 olmak üzere
# a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2 şeklinde yazılabilir. 

from fractions import gcd
from math import sqrt

def dickson(LIMIT):
    pisagor = set()
    mak = 0
    for s in range(3, int(sqrt(LIMIT))+1, 2):
        for t in range(s-2, 0, -2):
                if(gcd(s,t)==1):
                    a = s*t
                    b = int((s**2-t**2)/2)
                    c = int((s**2+t**2)/2)
                    if(a+b+c<=LIMIT):
                        pisagor.add((a,b,c))
    ucluler = []
    for i in range(LIMIT+1):
        ucluler.append(0)
    for triple in pisagor:
        l = sum(triple)
        for i in range(l, len(ucluler), l):
            ucluler[i] += 1
    return(ucluler.count(1))

print(dickson(1500000))

