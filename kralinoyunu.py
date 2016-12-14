#!/usr/bin/python3
# -*- coding: utf-8 -*-
liste=[]
n=int(input("oyun kaç kişiyle oynansın: "))
for i in range(1,n+1):
    liste.append(i)
i=1
while len(liste)!=1:
    liste[i%len(liste)]=0
    liste.remove(0)
    i=(i+1)%len(liste)
print(liste)
