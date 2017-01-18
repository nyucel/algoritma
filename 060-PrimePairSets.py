#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from sympy import primerange
from sympy import isprime
from itertools import permutations

primestest = list(primerange(3,10000))
toplam = 30000
sonuc = False
for n in primestest:
    for m in primestest[primestest.index(n)+1:]:
        if(isprime(int(str(n)+str(m)))==0 or isprime(int(str(m)+str(n)))==0):
            continue
        for p in primestest[primestest.index(m)+1:]:
            if(isprime(int(str(p)+str(m)))==0 or isprime(int(str(m)+str(p)))==0):
                continue
            for q in primestest[primestest.index(p)+1:]:
                if(n+m+p+q>toplam):
                    break
                if(isprime(int(str(p)+str(q)))==0 or isprime(int(str(q)+str(p)))==0):
                    continue
                for r in primestest[primestest.index(q)+1:]:
                    if(n+m+p+q+r>toplam):
                        break
                    if(isprime(int(str(r)+str(q)))==0 or isprime(int(str(q)+str(r)))==0):
                        continue
                    grup = permutations([n,m,p,q,r],2)
                    for i in grup:
                        if(isprime(int(str(i[0])+str(i[1])))==1):
                            continue
                        else:
                            break
                    else:
                        if(n+m+p+q+r<toplam):
                            toplam = n+m+p+q+r
                            sonuc = True
                            break
                if(sonuc):
                    break
            if(sonuc):
                break
        if(sonuc):
            break
    if(sonuc):
        break
print(toplam)
