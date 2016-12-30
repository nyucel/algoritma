#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
# Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
# Bu hali çok uzun sürede sonuç buluyor

a, b, n = 1, 1, 2
rakamlar = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while n<329000:
    a, b, n = b, a+b, n+1

while not (sorted(str(b)[:9])==rakamlar and sorted(str(b)[-9:])==rakamlar):
    a, b, n = b, a+b, n+1
print(n)
