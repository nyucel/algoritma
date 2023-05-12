#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functions import allprimes

def p(n):
    pn = liste[n-1]
    r = ((pn-1)**n+(pn+1)**n)%(pn**2)
    return(r)

n = 7035
liste=allprimes(250000)

while(p(n)<10**10):
    n += 1
print(p(n),n)
