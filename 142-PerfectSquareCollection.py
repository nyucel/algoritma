#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
# Bu soruda x,y,z üzerinde iterasyon yapmak neredeyse sonsuza kadar sürecek uzun bir iş olduğundan başka bir yöntem denenmeli.
# x+y=a, x-y=b, x+z=c, x-z=d, y+z=e, y-z=f (a,b,c,d,e,f tam kare olmak şartıyla) alındığında kolayca
# f=a-c, e=a-d ve b=c-e olduğu görülecektir. Bu eşitliklerin her biri aynı zamanda birer pisagor üçlüsünü de tarif eder (f^2+c^2=a^2 gibi).
# Her ne kadar 6 bilinmeyen var gibi görünse de bunlardan üçünü bildiğimizde kalan üçü onlar cinsinden hesaplanabilir.
# 6 değişken tam kare olarak hesaplandığında geri kalan sadece onlara karşılık gelen x,y,z üçlüsünü hesaplamak olacaktır.
# Aşağıdaki kod pisagor üçlüsü olma özelliği de kullanılarak daha verimli hale getirilebilir ama algoritma dersinde kullanmak için bu kadarını bırakıyorum.

from gmpy import is_square

def solve(a,b,c,d,e,f):
    x = (a+b)/2
    y = (e+f)/2
    z = (c-d)/2
    if(x>y and y>z and z>0 and x==int(x) and y==int(y) and z==int(z)):
        return(int(x+y+z))
    else:
        return(0)

for a in range(2,1000):
    a2 = a**2
    for c in range(2,1000):
        c2 = c**2
        for d in range(2,1000):
            d2 = d**2
            f2 = a2-c2
            if(f2>0 and is_square(f2)):
                e2 = a2-d2
                if(e2>0 and is_square(e2)):
                    b2 = c2-e2
                    if(b2>0 and is_square(b2)):
                        if(solve(a2,b2,c2,d2,e2,f2)!=0):
                            print(solve(a2,b2,c2,d2,e2,f2))
                            break
