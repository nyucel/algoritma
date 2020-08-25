#!/usr/bin/python3
# -*- coding: utf-8 -*-
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from fonksiyon import divisors

def list_diff(list1, list2):
        return (list(set(list1) - set(list2)))

liste = []
for n in range(11,28123):
    if(sum(divisors(n))>n):
        liste.append(n)

toplamlar = set()
for p in liste:
    for q in liste:
        if(p+q<28123):
            toplamlar.add(p+q)
sayilar = list(range(1,28123))
print(sum(list_diff(sayilar,toplamlar)))
