#!/usr/bin/python3
# -*- coding: utf-8 -*-
# A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.
# How many squarefree numbers are there below 2^50?

from functions import squarefree

print(squarefree(2**50))
