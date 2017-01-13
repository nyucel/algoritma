#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
# Burada c'yi 1'den başlatmamızın nedeni ardışık asal sayılar olan 2 ve 3'ü hesaba katmaktır.

from sympy import divisor_count

c = 1
for n in range(2,10**7):
    m=divisor_count(n)
    if(m==2):
        continue
    if(m==divisor_count(n+1)):
        c += 1
print(c)
