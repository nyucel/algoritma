#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
# There are 120 reversible numbers below one-thousand.
# How many reversible numbers are there below one-billion (10^9)?
# Çözümü yaklaşık 20 dk'da bulabiliyor

sayac = 0
cift = ["0","2","4","6","8"]
for n in range(1,10**9):
    if(n%10==0):
        continue
    reversen = n+int(str(n)[::-1])
    if(reversen%2==1):
        for m in cift:
            if(m in list(str(reversen))):
                break
        else:
            sayac += 1
print(sayac)
