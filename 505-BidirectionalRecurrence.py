#!/usr/bin/python3
# -*- coding: utf-8 -*-
# özyinelemeli fonksiyon örneği olarak bakalım, sorunun çözümünü vermiyor bu hali :)

def x(n):
    if(n==0):
        sonuc = 0
    elif(n==1):
        sonuc = 1
    elif(n>1 and n%2==0):
        sonuc = (3*x(int(n/2))+2*x(int(n/4)))%2**60
    else:
        sonuc = (2*x(int((n-1)/2))+3*x(int((n-1)/4)))%2**60
    return(sonuc)

def y(n,k):
    if(k>=n):
        sonuc = x(k)
    else:
        temp=[y(n,2*k),y(n,2*k+1)]
        sonuc = 2**60-1-max(temp)
    return(sonuc)

def A(n):
    return(y(n,1))

print(A(10000))
