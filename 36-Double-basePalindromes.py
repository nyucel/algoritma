#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The decimal number, 585 = 1001001001(base 2) (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def ispalindrome(n):
        if(str(n)==str(n)[::-1]):
            return(1)
        else:
            return(0)

sonuc = 0
for n in range(1,1000000):
    if(ispalindrome(n)==1 and ispalindrome(int(bin(n)[2:]))==1):
        sonuc += n
print(sonuc)
