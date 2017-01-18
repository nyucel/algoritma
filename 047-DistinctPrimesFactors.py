#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
#    644 = 2² × 7 × 23
#    645 = 3 × 5 × 43
#    646 = 2 × 17 × 19.
#    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from functions import allprimes
def primedivisors(m):
    carpanlar = []
    i,n=2,m
    while (i<=m/2):
        if n%i==0:
            carpanlar.append(i)
            n = n/i
        else:
            i += 1
    sonuc = []
    while not(len(carpanlar)==0):
        a=carpanlar.count(carpanlar[0])
        sonuc.append(carpanlar[0]**a)
        carpanlar = carpanlar[a:]
    return(sonuc)

asal = allprimes(200000)
for n in range(130000,200000):
    if(asal.count(n)==1):
        continue
    a = primedivisors(n)
    if(asal.count(n+1)==1):
        continue
    b = primedivisors(n+1)
    if(asal.count(n+2)==1):
        continue
    c = primedivisors(n+2)
    if(asal.count(n+3)==1):
        continue
    d = primedivisors(n+3)
    if(len(a)!=4 or len(b)!=4 or len(c)!=4 or len(d)!=4):
        continue
    for i in a:
        if(b.count(i)==1):
            break
    else:
        print(n,n+1,n+2,n+3)
        break
