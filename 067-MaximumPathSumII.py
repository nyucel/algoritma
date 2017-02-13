#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.

dosya=open("p067_triangle.txt")
triangle = []

for line in dosya.readlines():
    line = line.rstrip('\n').split(' ')
    triangle.append(line)
dosya.close()

for n in range(len(triangle)-2,-1,-1):
    for m in range(len(triangle[n])):
        triangle[n][m] = int(triangle[n][m]) +  max(int(triangle[n+1][m]),int(triangle[n+1][m+1]))

print(triangle[0][0])
