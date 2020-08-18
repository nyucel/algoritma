#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same number of positive divisors.

bolenler = [2]*(10**7+1)
sayac = 0

for i in range(2, len(bolenler)//2):
    for j in range(i*2, len(bolenler), i):
        bolenler[j] += 1

for i in range(2,len(bolenler)-1):
    if(bolenler[i]==bolenler[i+1]):
        sayac += 1

print(sayac)
