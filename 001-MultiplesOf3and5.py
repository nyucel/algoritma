#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the sum of all the multiples of 3 or 5 below 1000.
n = set()
for i in range(1000):
    if(i%3==0 or i%5==0):
        n.add(i)
print(sum(n))
