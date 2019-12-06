#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

bolenler = [2]*(10**7+1)
sayac = 0

for i in range(2, len(bolenler)//2):
    for j in range(i*2, len(bolenler), i):
        bolenler[j] += 1

for i in range(2,len(bolenler)-1):
    if(bolenler[i]==bolenler[i+1]):
        sayac += 1

print(sayac)
