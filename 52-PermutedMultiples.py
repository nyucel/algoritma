#!/usr/bin/python3
# -*- coding: utf-8 -*-
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def samedigits(n,p):
    for i in str(n*p):
        if(list(str(n)).count(i)==0):
            return(0)
            break
    else:
        return(1)

for n in range(1,1000000):
    same = 0
    for p in range(2,7):
        if(samedigits(n,p)==1):
            same += 1
    if(same==5):
        print(n)
        break

