#!/usr/bin/python3
# -*- coding: utf-8 -*-
# What is the largest prime factor of the number 600851475143 ?
from functions import allprimes

primes=allprimes(10000)
number,i=600851475143,1
while not (number%primes[-i]==0):
    i +=1
print(primes[-i])
