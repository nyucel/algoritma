#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The prime 41, can be written as the sum of six consecutive primes:
#           41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from functions import isprime
from functions import allprimes

asal = allprimes(4000)
toplam = []
a,p = 0, 5

for p in range(5,len(asal)):
    for a in range(0,len(asal)-p):
        if(isprime(sum(asal[a:a+p]))==1 and sum(asal[a:a+p])<1000000):
            toplam.append([sum(asal[a:a+p]),p])
print(toplam[-1][0])
