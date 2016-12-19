#!/usr/bin/python3
# -*- coding: utf-8 -*-
# What is the largest prime factor of the number 600851475143 ?
from functions import isprime
primes=[]
number=600851475143
for i in range(2,10000):
    if isprime(i)==1:
        primes.append(i)
factor=[]
for i in primes:
    if number%i==0:
        factor.append(i)
print(factor[-1])
