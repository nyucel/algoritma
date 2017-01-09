#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functions import isprime

asal,n,p = 3,9,4

while (asal/(2*p+1)>0.1):
    for m in range(1,5):
        n += p
        if(isprime(n)==1):
            asal += 1
    p += 2
print(p+1)# p kadar ekleyince karenin bir kenarı p+1 oluyor
