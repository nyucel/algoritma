#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=173

LIMIT = 10**6
sonuc = 0

for n in range(1, 500):
    sonuc += (LIMIT//4)//n - n

print(sonuc)
