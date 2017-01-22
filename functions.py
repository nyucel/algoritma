#!/usr/bin/python3
# -*- coding: utf-8 -*-

def isprime(a):
    """bir sayının asal olup olmadığını kontrol eden fonksiyon"""
    i,prime=3,1
    if(a<2):
        prime=0
    if a!=2 and a%2==0:
        prime=0
    while prime!=0 and i<=a**(1/2):
        if a%i==0:
            prime=0
            break
        i += 2
    return(prime)

def ispandigital(n):
    """bir sayının pandigital sayı olup olmadığını kontrol eden fonksiyon"""
    number = []
    for i in str(n):
        number.append(int(i))
    for i in range(1,len(number)+1):
        if(number.count(i)==0):
            return(0)
    else:
        return(1)

def allprimes(n):
    """bir sayıdan küçük bütün asal sayıları dizi olarak döndüren fonksiyon"""
    primes=[]
    for i in range(2,n+1):
        primes.append(i)
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])

def divisors(n):
    """bir sayının bölenlerini bir dizi olarak geri döndüren fonksiyon"""
    carpanlar = [1]
    i=2
    while (i<=n/2):
        if n%i==0:
            carpanlar.append(i)
        i += 1
    return(carpanlar)

def squarefree(LIMIT):
    """Bir sayıdan küçük, hiç bir asal sayının karesine bölünmeyen sayıların sayısını döndüren fonksiyon"""
    from itertools import count
    N = int(LIMIT**(1/2))+1
    divisors = [0]*N
    for i in count(2):
        if(i**2>=LIMIT):
            break
        if(divisors[i]!=0):
            continue
        if(divisors[i]==-1):
            continue
        if(i**2<N):
            for j in range(i**2,N,i**2):
                divisors[j]=-1
        for j in range(i,N,i):
            if(divisors[j]==-1):
                continue
            divisors[j] += 1
    toplam=0
    for i in range(2,N):
        if(divisors[i]==-1):
            continue
        if(divisors[i]&1):
            toplam += LIMIT//(i**2)
        else:
            toplam -= LIMIT//(i**2)
    return(LIMIT-toplam)

def nCr(n,r):
    """n eleman içinden r'nin kaç farklı şekilde seçilebileceğini veren fonksiyon"""
    from math import factorial
    return(int(factorial(n)/(factorial(r)*factorial(n-r))))
