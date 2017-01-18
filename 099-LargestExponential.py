#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.
# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
# Using base_exp.txt, a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
# a^b ile c^d sayılarını karşılaştırmak yerine her iki tarafın logaritmasını alıp öyle karşılaştırma yapmak aynı şey olacaktır.
# Böyle yapınca karşılaştırma b*log10(a) ile d*log10(c) arasında olacak ve çok hızlıca yapılabilecektir.

from math import log10

dosya=open("p099_base_exp.txt")

enbuyuk = 0
satir = 1

for line in dosya.readlines():
    [a, b] = line.rsplit(',')
    sayi = int(b)*log10(int(a))

    if(sayi>enbuyuk):
        enbuyuk = sayi
        sonuc = satir

    satir += 1
print(sonuc)
