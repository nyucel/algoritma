#!/usr/bin/python3
# -*- coding: utf-8 -*-

def isprime(a):
    """bir sayının asal olup olmadığını kontrol eden fonksiyon"""
    i,prime=3,1
    if a!=2 and a%2==0:
        prime=0
    while prime!=0 and i<=a**(1/2):
        if a%i==0:
            prime=0
            break
        i += 2
    return(prime)

def divisors(n):
    """bir sayının bölenlerini bir dizi olarak geri döndüren fonksiyon"""
    carpanlar = [1]
    i=2
    while (i<=n/2):
        if n%i==0:
            carpanlar.append(i)
        i += 1
    return(carpanlar)
