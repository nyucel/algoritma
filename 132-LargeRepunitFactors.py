#!/usr/bin/python3
# -*- coding: utf-8 -*-
# A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.
# For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.
# Find the sum of the first forty prime factors of R(10^9).
# https://en.wikipedia.org/wiki/Repunit adresinden de görülebileceği gibi bu sayılar R(n)=10^n-1 şeklinde yazılabiliyor.
# n asal sayısının (10^(10^9) - 1)'i bölmesi gerektiğini biliyoruz. Bu nedenle python'un pow fonksiyonunu kullanarak sonucu bulmak çok kolay oluyor.
# pow kullanmak yerine 10**L%n yazmayı denediğinizde işlemlerin süresinin karşılaştırılamayacak kadar uzun sürdüğünü görebilirsiniz.

from sympy import primerange

primes = primerange(5,1000000)

bolen = []
L = 10**9

for n in primes:
    if(pow(10, L, n) == 1):
        bolen.append(n)
        if(len(bolen)==40):
            break
print(sum(bolen))
