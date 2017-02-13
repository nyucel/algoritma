#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=81

dosya=open("p081_matrix.txt")
matrix = []
for line in dosya.readlines():
    line = line.rstrip('\n').split(',')
    matrix.append(line)
dosya.close()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(i!=0 and j!=0):
            matrix[i][j] = int(matrix[i][j]) +  min(int(matrix[i-1][j]),int(matrix[i][j-1]))
        elif(i>0):
            matrix[i][j] = int(matrix[i][j]) +  int(matrix[i-1][j])
        elif(j>0):
            matrix[i][j] = int(matrix[i][j]) +  int(matrix[i][j-1])

print(matrix[len(matrix)-1][len(matrix[0])-1])
