#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.
# What is the sum of all such integers n below 150 million?
# Verilen şartları sağlayan n sayısının 10'un katı olması ve 3,7, ve 13'e bölünmemesi gerektiği kolayca görülebilir.
# 144774340 sayısı da n^2+1, n^2+3, n^2+7, n^2+9, n^2+13 ve n^2+27 için asal sayılar üretmekte ama aynı zamanda n^2+21 için de asal ürettiğinden sonuçta ortaya çıkan dizinin ardışık olma özelliğini bozmasına dikkat ediyoruz.
# 3'ten büyük bütün asal sayıların 6'ya göre mod'ları -1 veya +1'dir.

from sympy import isprime

toplam=0
LIMIT = 150000000

for n in range(10,LIMIT,10):
    if(n%3==0 or n%7==0 or n%13==0):
        continue
    m = n**2+1
    if(m%6!=1 and m%6!=5):
        continue
    if(isprime(m)==1):
        if(isprime(m+2)==1):
            if(isprime(m+6)==1):
                if(isprime(m+8)==1):
                    if(isprime(m+12)==1):
                        if(isprime(m+20)!=1):
                            if(isprime(m+26)==1):
                                toplam += n
print(toplam)
