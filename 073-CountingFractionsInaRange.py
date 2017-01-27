
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gmpy import mpq

liste = set()
LIMIT = 12000

for n in range(1, LIMIT+1):
    for m in range(2*n, LIMIT+1):
        if(mpq(n,m)<mpq(1,3)):
            continue
        liste.add(mpq(n,m))
p = sorted(liste).index(mpq(1,3))
q = sorted(liste).index(mpq(1,2))

print(q-p-1)
