#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#Find the least number for which the proportion of bouncy numbers is exactly 99%.

def comparison(i):
    increasing, decreasing="FALSE", "FALSE"
    for j in range(len(str(i))-1):
        if int(str(i)[j])>int(str(i)[j+1]):
            decreasing="TRUE"
        elif int(str(i)[j])==int(str(i)[j+1]):
            pass
        else:
            increasing="TRUE"
    if increasing=="TRUE" and decreasing=="TRUE":
        return 1
    else:
        return 0

bouncy,x=0,100
while (bouncy/x)<0.99:
    if(comparison(x)==1):
        bouncy +=1
    x +=1
print(x)
