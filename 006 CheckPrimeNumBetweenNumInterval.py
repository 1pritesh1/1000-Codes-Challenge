# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:05:45 2021

@author: Pritesh
"""

low = 200
high = 300

print("Prime number between",low, " and ",high, "are:")

for num in range(low,high+1):
    if num > 1:
        for i in range(2,num):
            if(num % i)==0:
                break
        else:
            print(num)