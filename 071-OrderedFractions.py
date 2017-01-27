
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Aradığımız kesir 3/7'ye çok yakın olacağından n'i 1'den 10^6'ya kadar arttırırken m'i de n/m~=3/7 olacak şekilde m=7n/3 ile başlatıp 3/7'ye çok yakın olan 299999/700000 ile kıyaslıyoruz.
from gmpy import mpq

liste = set()
LIMIT = 10**6

for n in range(1, LIMIT+1):
    for m in range((7*n//3), LIMIT+1):
        if(mpq(n,m)<mpq(299999,700000)):
            break
        if(mpq(n,m)>mpq(3,7)):
            continue
        liste.add(mpq(n,m))
p = sorted(liste).index(mpq(3,7))

print(sorted(liste)[p-1])
