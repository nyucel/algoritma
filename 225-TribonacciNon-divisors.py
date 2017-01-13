#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
# is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.
# It can be shown that 27 does not divide any terms of this sequence.
# In fact, 27 is the first odd number with this property.
# Find the 124th odd number that does not divide any terms of the above sequence.
# Bir n sayısı bu dizinin elemanlarından birini bölüyorsa t3%n=0 olmalı. 
# Dizinin elemanlarının n'e göre mdu alınırsa mutlaka elemanların (1,1,1) olduğu bir döngüye giriyor. 
# Bunun için dizinin bu döngüye girene kadarki kısmına bakmak n'in bölmeyen sayılardan biri olup olmadığını anlamak için yeterli.

bolmeyensayisi, n = 0, 3
while bolmeyensayisi < 124:
    t1, t2, t3 = 1, 1, 3
    while t3>0 and (t1,t2,t3) != (1,1,1):
        t1, t2, t3 = t2, t3, (t1 + t2 + t3) % n
    if t3>0:
        bolmeyensayisi += 1
    n += 2
print(n-2)
