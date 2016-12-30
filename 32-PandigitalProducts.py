#!/usr/bin/python3
# -*- coding: utf-8 -*-
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from functions import ispandigital

carpimlar=[]
for a in range(1,500):
    for b in range(1,2000):
        q=''.join([str(a),str(b),str(a*b)])
        if(len(str(q))==9 and ispandigital(q)==1):
            carpimlar.append(a*b)
carpimlar.sort()

for n in carpimlar:
    while not (carpimlar.count(n)==1):
        carpimlar.remove(n)
print(sum(carpimlar))
