#!/usr/bin/python3
# -*- coding: utf-8 -*-
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

dizi = '0'
i = 1

while len(dizi)<1000005:
    dizi = dizi+str(i)
    i += 1
print(int(dizi[1])*int(dizi[10])*int(dizi[100])*int(dizi[1000])*int(dizi[10000])*int(dizi[100000])*int(dizi[1000000]))
