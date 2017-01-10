#!/usr/bin/python3
# -*- coding: utf-8 -*-
# For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.
# For example, if p=7,
# (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
# As 872 mod(7) = 4, S(7) = 4.
# It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.
# Find ∑S(p) for 5 ≤ p < 108.
# Soruda verilen S fonksiyonu (p-5)!+(p-4)!+(p-3)!+(p-2)!+(p-1)! (mod p) şeklinde yazılabilir.
# Bu ifadeyi (p-1)! parantezine alıp (p-2)(mod p) yerine -2 yazıldığında 
# (elbette diğerleri için de aynı şeyi yaparak) ve Wilson Teoremini kullanarak S(p)=-3/8(mod p) sonucuna ulaşılır.
# Buradan da S(p)=(p-3)/8 (mod p) elde edilir.
# Kolayca S(p)'nin ancak p'nin asal olduğu durumlarda sıfırdan farklı değer verdiği görülebilir.
# p'nin asal olduğu bilinince Fermatın Küçük Teoremi kullanılarak paydadaki 8'in tersi bulunabilir.

from functions import allprimes

def s(p):
    return(((p-3)*pow(8,p-2,p))%p)

primes = allprimes(10**8)[2:]
cozum = 0

for p in primes:
    cozum += s(p)

print(cozum)
