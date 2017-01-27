#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Burada paydaya yazacağımız her n değeri için onunla arasında asal olan sayıların sayısını bulmak yeterli. Sonuç da bu sayıların toplamından oluşuyor. 

from sympy import totient

LIMIT = 10**6
sonuc = 0
for n in range(1,LIMIT+1):
    sonuc += totient(n)
print(sonuc-1)
