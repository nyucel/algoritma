#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

sonuc = 0
for p in range(1,10):
    for q in range(1,22):
        if(len(str(p**q))==q):
            sonuc += 1
print(sonuc)
