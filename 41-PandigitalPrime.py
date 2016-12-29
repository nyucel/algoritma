#!/usr/bin/python3
# -*- coding: utf-8 -*-
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from functions import allprimes
from functions import ispandigital

primes=allprimes(10000000)[::-1]

for n in primes:
    if(ispandigital(n)==1):
        print(n)
        break
