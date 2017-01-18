#!/usr/bin/python3
# -*- coding: utf-8 -*-
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

sonuc = 1
for a in range(11,100):
    if(a%10!=0):
        for n in range(1,10):
            c=a%10*10+n
            if(c%11!=0):
                if(a/c==int(a/10)/n):
                    sonuc *= c/a
print(int(sonuc))
