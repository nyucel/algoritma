#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    toplam = 1
    q = int(n**(1/2)//1)+1
    for p in range(2, q):
        if(n%p==0):
            toplam += p + n/p
    if((q-1)**2==n):
        return(int(toplam-q))
    return(int(toplam))

gtoplam = 0
for m in range(2,10000):
    s = d(m)
    if(m==s):
        continue
    if(s>10000):
        continue
    if(m==d(s)):
        gtoplam += m
print(gtoplam)
