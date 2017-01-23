#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.
# How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

from sympy import primerange

sprimes = list(primerange(2,10**8))
primes = []
for n in sprimes:
    if(len(str(n))==len(set(str(n))) and list(str(n)).count("0")==0):
        primes.append(str(n))

# 9 basamaklı hiçbir pandijital sayı asal olamayacağından üst değer 10^8'e kadar alınmıştır.
# Bu işlem sonunda içinde 0 bulunan (1049 gibi) ve bir rakamı tekrarlı şekilde içeren (113 gibi) asal sayıları çıkartıyoruz.
# Çünkü onları kullanıp 9 basamaklı bir pandijital sayı üretmek mümkün değil.
# Bu işlemin sonunda denenmesi gereken asal sayı sayısı 5761455'den 43089'a düşüyor.
# Bu soru 9 basamaklı pandijital sayıların altkümelerinin kombinasyonlarını deneyerek de çözülebilir. Muhtemelen daha kısa sürede de çözüm bulacaktır.
# Aşağıdaki yöntemde ise en fazla 6 farklı asal sayının bir araya getirilip bir 9 basamaklı pandijital sayı üretebileceği kullanılmıştır.
# Aynı grubu tekrar eklememek için küme kavramı kullanılmıştır. Kümeler eleman olarak listeleri alamadığından çözümü veren kümeler önce sıralanış, sonra da tuple tipine dönüştürülerek kümeye eklenmiştir. Böylece iki farklı asal sayıyı veren {2,5,47,89,631} ve {5,2,47,89,631} kümeleri bir defa sayılmıştır.
# Kullanılan sayi1, sayi2 gibi değişkenler yerine bir sayı[j] listesi oluşturulmasını derste vereceğim ödev olarak buraya bırakıyorum :)

sonuc = set()
for a in primes:
    for b in primes:
        sayi1 = a + b
        if(len(sayi1)>9):
            break
        if(len(sayi1)!=len(set(sayi1))):
            continue
        if(len(sayi1)==9):
            sonuc.add(tuple(sorted([a,b])))
        for c in primes:
            sayi2 = sayi1 + c
            if(len(sayi2)>9):
                break
            if(len(sayi2)!=len(set(sayi2))):
                continue
            if(len(sayi2)==9):
                sonuc.add(tuple(sorted([a,b,c])))
            for d in primes:
                sayi3 = sayi2 + d
                if(len(sayi3)>9):
                    break
                if(len(sayi3)!=len(set(sayi3))):
                    continue
                if(len(sayi3)==9):
                    sonuc.add(tuple(sorted([a,b,c,d])))
                for e in primes:
                    sayi4 = sayi3 + e
                    if(len(sayi4)>9):
                        break
                    if(len(sayi4)!=len(set(sayi4))):
                        continue
                    if(len(sayi4)==9):
                        sonuc.add(tuple(sorted([a,b,c,d,e])))
                    for f in primes:
                        sayi5 = sayi4 + f
                        if(len(sayi5)>9):
                            break
                        if(len(sayi5)!=len(set(sayi5))):
                            continue
                        if(len(sayi5)==9):
                            sonuc.add(tuple(sorted([a,b,c,d,e,f])))
print(len(sonuc))
