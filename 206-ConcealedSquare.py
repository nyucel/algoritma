#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
#where each “_” is a single digit.

n = 10**9
while(True):
    m = str(n*n)
    if(m[0]=="1" and m[2]=="2" and m[4]=="3" and m[6]=="4" and m[8]=="5" and m[10]=="6" and m[12]=="7" and m[14]=="8" and m[16]=="9"):
        print(n)
        break
    n += 10
