#!/usr/bin/python3
# -*- coding: utf-8 -*-
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date

sonuc = 0
for yil in range(1901,2001):
    for ay in range(1,13):
        if(date(yil,ay,1).weekday()==6):
            sonuc += 1
print(sonuc)
