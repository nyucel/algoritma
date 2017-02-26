#!/usr/bin/python3
# -*- coding: utf-8 -*-
#1'den 10'a kadar bütün sayılara kalansız bölünen en küçük sayı 2520'dir.
#1'den 20'ye kadar bütün sayılara kalansız bölünen en küçük positif sayı kaçtır?
#-----------------İLK 20 SAYI İÇİN YAZILMIŞTIR..---------------
#ÖNEMLİ= 15'e bölünmesi demek 3 ve 5'e , 16'ya bölünmesi ise 4 tane 2 ye bölünmesi demektir.
#i değerini 15'e çekip "2"sayısının adetinin 3'e düştüğünü görebilirsiniz.
i,carpım=20,1
l=[]
while i>1 :
    if i%2==0 or i%3==0 or i%5==0 or i%7==0 :
        a,j=i,2
        while a>1 :
            if a==j**2 :
               l.append(j)
               carpım=carpım*j
            if a%j==0:
                a=a/j
                if l.count(j)==0:
                    l.append(j)
                    carpım=carpım*j 
            else:
                j+=1
    else:
        if l.count(i)==0:
            l.append(i)  
            carpım=carpım*i
    i-=1
l.sort()
print(l)
print(carpım)
        
