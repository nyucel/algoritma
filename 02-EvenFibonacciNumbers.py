#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dört milyondan küçük çift Fibonacci sayılarının toplamını bulan program
a,b,c,toplam=1,1,0,0
while c<4000000:
    if c%2==0:
        toplam=toplam+c
    c=a+b
    a,b=b,c
print(toplam)
