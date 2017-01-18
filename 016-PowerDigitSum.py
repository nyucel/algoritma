#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

number = str(2**1000)
sonuc = 0
for n in number:
    sonuc += int(n)
print(sonuc)
