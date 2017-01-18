#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
sonuc=1
for a in range(2,100):
    for b in range(2,100):
        c=a**b
        toplam=0
        for i in str(c):
            toplam += int(i)
        if(toplam>sonuc):
            sonuc=toplam
print(sonuc)
