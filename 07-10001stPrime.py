#!/usr/bin/python3
# -*- coding: utf-8 -*-
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from functions import isprime

n,p = 0,1
while n<10001:
    p += 1
    if(isprime(p)==1):
        n += 1
print(p)

