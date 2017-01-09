#!/usr/bin/python3
# -*- coding: utf-8 -*-

from decimal import *

getcontext().prec = 3000

def desen(dizi):
    for n in range(2,3000):
        if(dizi[:n]==dizi[n:2*n]):
            return(n)
            break

enuzun,sonuc = 0,0

for p in range(2,1000,1):
    n = str(1/Decimal(p)).split(".")[1]
    if(desen(n)==None):
        continue
    elif(desen(n)>enuzun):
        enuzun, sonuc = desen(n), p

print(sonuc)
