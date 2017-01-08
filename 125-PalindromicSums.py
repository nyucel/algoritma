#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.
# There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.
# Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.

toplam = set()
for n in range(1,10001):
    karetoplami = n**2
    for m in range(n+1,10001):
        karetoplami += m**2
        if(karetoplami>10**8):
            break
        if(str(karetoplami)==str(karetoplami)[::-1]):
            toplam.add(karetoplami)
print(sum(toplam))
        
