#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
# What is the expected number of distinct colors in 20 randomly picked balls?
# Give your answer with nine digits after the decimal point (a.bcdefghij).

from functions import nCr

print(str(7*(1-(nCr(60,20)/nCr(70,20))))[:11])
