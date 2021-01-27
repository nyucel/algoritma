#!/usr/bin/python3
# -*- coding: utf-8 -*-
#7 basamaklı en büyük sayı 9999999. onun da basamaklarındaki rakamların karelerinin toplamı 7*9^2=567

def karetoplam(n):
    toplam = 0
    while(n):
        toplam += (n%10)*(n%10)
        n = n//10
    return(toplam)

seksendokuz = set()

for p in range (2,568):
    x = p
    while(x!=1 and x!=89):
        x = karetoplam(x)
    if(x==89):
        seksendokuz.add(p)

cozum = len(seksendokuz)

for n in range(568,10000000):
    if(karetoplam(n) in seksendokuz):
        cozum += 1

print(cozum)
