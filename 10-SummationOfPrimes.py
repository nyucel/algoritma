#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the sum of all the primes below two million.
from functions import isprime
toplam = 0
for i in range(2,2000000):
    if isprime(i)==1:
        toplam += i
print(toplam)
