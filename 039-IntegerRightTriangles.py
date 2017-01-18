#!/usr/bin/python3
# -*- coding: utf-8 -*-
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

enfazla = 3
for p in range(120,1001):
    cozumsayisi = 0
    for a in range(20,401):
        for b in range(40,401):
            c=p-a-b
            if(c<0 or c>(a+b)):
                continue
            if(c>0 and a**2+b**2==c**2):
                cozumsayisi += 1
            if(cozumsayisi>enfazla):
                enfazla=cozumsayisi
                pmax=p
print(pmax)
