#!/usr/bin/python3
# -*- coding: utf-8 -*-
n=int(input("oyun kaç kişiyle oynansın: "))
liste = list(range(1, n+1, 1))
i=1
while(len(liste)!=1):
    liste[i%len(liste)]=0
    liste.remove(0)
    i=(i+1)%len(liste)
print(liste[0])
