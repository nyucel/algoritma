#!/usr/bin/python3
# -*- coding: utf-8 -*-
#7 basamaklı en büyük sayı 9999999. onun da basamaklarındaki rakamların karelerinin toplamı 7*9^2=567
#1'e ulaşan sayıların sayısı çok daha az olduğundan onların sayısını bulup 10 milyondan çıkartmak daha küçük bir listeyle çalışmaya imkan verir.

def karetoplam(n):
    toplam = 0
    while(n):
        toplam += (n%10)*(n%10)
        n = n//10
    return(toplam)

birler = {1}

for p in range (2,568):
    x = p
    while(x!=1 and x!=89):
        x = karetoplam(x)
    if(x==1):
        birler.add(p)

cozum = len(birler)

for n in range(568,10000000):
    if(karetoplam(n) in birler):
        cozum += 1

print(9999999-cozum)
