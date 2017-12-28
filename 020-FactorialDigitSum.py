#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the sum of the digits in the number 100!
from math import factorial
sonuc = 0
for i in str(factorial(100)):
    sonuc += int(i)
print(sonuc)
