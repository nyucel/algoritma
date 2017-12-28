#!/usr/bin/python3
# -*- coding: utf-8 -*-
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from functools import reduce
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
def lcmm(*args):
    return reduce(lcm, args)

print(lcmm(20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2))
