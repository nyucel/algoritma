#!/usr/bin/python3
# -*- coding: utf-8 -*-
# the sum of all the numbers that can be written as the sum of fifth powers of their digits.
toplam=0
for i in range(1000,354294):
    control=0
    for j in str(i):
        control += int(j)**5
    if i==control:
        toplam += control
print(toplam)
