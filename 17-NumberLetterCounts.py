#!/usr/bin/python3
# -*- coding: utf-8 -*-
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

teens = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def donustur(n):
    if(n<20):
        return(teens[n])
    elif(n<100):
        return(tens[int(n/10)] + teens[n%10])
    elif(n<1000):
        if(n%100==0):
            return(teens[int(n/100)]+"hundred")
        else:
            return(teens[int(n/100)]+"hundred"+"and"+donustur(n%100))
    else:
        return("onethousand")

sonuc = 0

for i in range(1,1001):
    sonuc += len(donustur(i))

print(sonuc)
