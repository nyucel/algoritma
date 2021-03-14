#!/usr/bin/python3
# -*- coding: utf-8 -*-

LIMIT = 10**8
enkucuk = [0] * (LIMIT + 1)

for i in range(2, len(enkucuk)):
    if enkucuk[i] == 0:
        kuvvet = 1
        j = i
        while(kuvvet<LIMIT//2):
            kuvvet *= i
            for k in range(kuvvet, len(enkucuk), kuvvet):
                enkucuk[k] = max(j, enkucuk[k])
            temp = j // i
            while temp % i == 0:
                kuvvet *= i
                temp //= i
            j += i

print(sum(enkucuk))
