#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.
# We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
# You are given that a2 = 512 and a10 = 614656.
# Find a30.

def digitsum(n):
    return(sum(map(int,str(n))))

cozum = []
for n in range(2,100):
    for m in range(2,10):
        p = n**m
        if(n==digitsum(p)):
            cozum.append(p)
cozum.sort()
print(cozum[29])

