#!/usr/bin/python3
# -*- coding: utf-8 -*-

sonuc,payda,pay = 0,0,1

for n in range(1000):
    payda,pay = pay,2*pay+payda
    if(len(str(pay-payda))>len(str(payda))):
        sonuc +=1

print(sonuc)
