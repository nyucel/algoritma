#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Soruyu ilk okuduğunuzda aranan serinin ilk elemanının triangle, ikincinin square dizisinden alınması gerekiyormuş gibi görünüyor ama öyle bir çözüm yok. Soruda istenen altılnın her birinin başka bir diziden olması. İkinci özellik olan farklı indeks numarasına bakmaya gerek yok tek bir çözüm var çünkü.

from itertools import permutations

triangle,square,pentagonal,hexagonal,heptagonal,octagonal = [], [], [],[], [], []

for n in range(1,141):
    if(len(str((n*(n+1)//2)))==4):
        triangle.append(n*(n+1)//2)
    if(len(str(n**2))==4):
        square.append(int(n**2))
    if(len(str(n*(3*n-1)//2))==4):
        pentagonal.append(n*(3*n-1)//2)
    if(len(str(n*(2*n-1)))==4):
        hexagonal.append(n*(2*n-1))
    if(len(str(n*(5*n-3)//2))==4):
        heptagonal.append(n*(5*n-3)//2)
    if(len(str(n*(3*n-2)))==4):
        octagonal.append(int(n*(3*n-2)))
liste = list(permutations((triangle,square,pentagonal,hexagonal,heptagonal,octagonal),6))

for dizi in liste:
    for n0 in dizi[0]:
        for n1 in dizi[1]:
            if(str(n0)[2:]==str(n1)[:2]):
                for n2 in dizi[2]:
                    if(str(n1)[2:]==str(n2)[:2]):
                        for n3 in dizi[3]:
                            if(str(n2)[2:]==str(n3)[:2]):
                                for n4 in dizi[4]:
                                    if(str(n3)[2:]==str(n4)[:2]):
                                        for n5 in dizi[5]:
                                            if(str(n4)[2:]==str(n5)[:2] and str(n5)[2:]==str(n0)[:2]):
                                                print(n0+n1+n2+n3+n4+n5)
