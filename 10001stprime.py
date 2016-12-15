#!/usr/bin/python3
# -*- coding: utf-8 -*-
#10001. asal sayı nedir?
primes=[2,3]
n=5
while len(primes)<10001:
    i=3
    asalmi=0
    while i<=n**(1/2):
        if n%i==0:
            asalmi=1
        i=i+2
    if asalmi==0:
        primes.append(n)
    n=n+2
print(primes[10000])
