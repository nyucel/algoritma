#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
sum=0
for i in range(1,1001):
    sum += i**i
print(sum%(10**10))
