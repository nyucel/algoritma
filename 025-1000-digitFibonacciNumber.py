#!/usr/bin/python3
# -*- coding: utf-8 -*-
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
a, b, n = 1, 1, 2
while len(str(b))<1000:
    a, b, n = b, a+b, n+1
print(n)
