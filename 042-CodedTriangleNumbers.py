#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt a 16K text file containing nearly two-thousand common English words, how many are triangle words?

dosya=open("p042_words.txt")
for line in dosya.readlines():
        words = line.rstrip('\n').split('","')

sonuc = 0
triangle = []
alfabe=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for n in range(1,20):
    triangle.append(n*(n+1))
for p in words:
    toplam = 0
    for i in p:
        toplam += alfabe.index(i)+1
    if(triangle.count(toplam*2)==1):
        sonuc += 1
print(sonuc)
