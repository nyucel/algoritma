#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=62

cubes = []
for n in range(4600,10000):
    cubes.append(n**3)

for n in cubes:
    tekrar = 0
    for m in cubes[cubes.index(n)+1:]:
        if(sorted(str(n))==sorted(str(m))):
            tekrar += 1
    if(tekrar==4):
        print(n)
        break
